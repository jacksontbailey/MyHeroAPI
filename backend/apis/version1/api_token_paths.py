from fastapi import APIRouter, Body, HTTPException, Depends
from schemas.schema_token import ApiTokenCreate, ApiTokenEdit
from db.repository.token import save_api_key, change_api_key_status, add_api_keys, delete_api_key, encode_tokens, decode_tokens
from db.repository.users import get_current_active_user
from core.security_funct import generate_random_token
from core.config import settings


router = APIRouter()


@router.post("/create")
async def create_api_token(token: ApiTokenCreate):
    """
    Create a new api token.
    """
    print("started backend")
    new_token = await generate_random_token()
    print(f"New token is: {new_token}")
    encrypted_token = await encode_tokens(new_token)
    print(f"Encrypted token is: {new_token}")
    save_api_key(token.username, encrypted_token, token.name, token.hasExpiration, token.expiration, token.status)
    add_api_keys(token.username, encrypted_token, token.name, token.hasExpiration, token.expiration, token.status)
    
    return {"token": new_token}



@router.get("/list-keys")
async def list_api_tokens(user = Depends(get_current_active_user)):
    """
    List all the api keys for a user.
    """
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    user_data = settings.USER_COLL.find_one({"username": user.username})
    if not user_data or "api_keys" not in user_data:
        raise HTTPException(status_code=404, detail="API keys not found for this account.")
    api_keys = list(user_data.get("api_keys"))
    decoded_api_keys = decode_tokens(api_keys)

    return decoded_api_keys



@router.put("/edit-key")
async def edit_api_key(api_key: ApiTokenEdit = Body(..., example={'token': 'your_api_token', 'status': 'inactive'})):
    """
    Edit the status of an api key.
    """ 
    try:
        encoded_token = await encode_tokens(api_key.token)
        final_encoded_token = await encode_tokens(encoded_token)
        change_api_key_status(final_encoded_token, api_key.status)
        return {"message": "API key status updated successfully"}
    except:
        raise HTTPException(status_code=400, detail="Failed to update API key status")



@router.delete("/delete-key")
async def delete_inactive_api_key(key: str):
    """
    Delete an api key with a status of inactive.
    """

    encoded_key = await encode_tokens(raw_key=key)
    api_key = settings.API_COLL.find_one({"api_key": encoded_key})
    print(f"total match: \n {api_key}")
    if api_key and (api_key['key_status'] == "inactive"):
        await delete_api_key(api_key['username'], encoded_key)
        return {"message": "API key deleted"}
    else:
        raise HTTPException(status_code=400, detail="Cannot delete active api key")

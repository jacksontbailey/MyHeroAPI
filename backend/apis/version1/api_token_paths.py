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
    new_token = generate_random_token()
    encrypted_token = encode_tokens(new_token)
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
    decoded_api_keys = await decode_tokens(api_keys)
    final_decoded_keys = await decode_tokens(decoded_api_keys)

    return final_decoded_keys



@router.patch("/update-status")
async def edit_api_key(key: str, status: str, user = Depends(get_current_active_user)):
    """
    Edit the status of an api key.
    """ 
    try:
        encoded_token = await encode_tokens(key)
        final_encoded_token = await encode_tokens(encoded_token)
        change_api_key_status(username = user.username, key = final_encoded_token, status = status)
        return {"message": "API key status updated successfully"}
    except:
        raise HTTPException(status_code=400, detail="Failed to update API key status")



@router.delete("/delete-key")
async def delete_inactive_api_key(key: str):
    """
    Delete an api key with a status of inactive.
    """

    encoded_key = await encode_tokens(raw_key=key)
    final_encoded_token = await encode_tokens(encoded_key)
    api_key = settings.API_COLL.find_one({"api_key": final_encoded_token})
    print(f"total match: \n {api_key}")
    if api_key and (api_key['key_status'] == "inactive"):
        await delete_api_key(api_key['username'], final_encoded_token)
        return {"message": "API key deleted"}
    else:
        raise HTTPException(status_code=400, detail="Cannot delete active api key")

from fastapi import APIRouter, Body, HTTPException, Depends
from schemas.schema_token import ApiTokenCreate, ApiTokenEdit
from db.repository.token import save_api_key, change_api_key_status, add_api_keys, delete_api_key, decode_tokens
from db.repository.users import get_current_active_user
from core.security_funct import generate_random_token
from core.config import settings


router = APIRouter()


@router.post("/create")
async def create_api_token(token: ApiTokenCreate):
    """
    Create a new api token.
    """
    new_token = await generate_random_token()
    await save_api_key(token.username, new_token, token.name, token.hasExpiration, token.expiration, token.status)
    await add_api_keys(token.username, new_token, token.name, token.hasExpiration, token.expiration, token.status)
    
    return {"token": new_token}



@router.get("/list")
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



@router.put("/edit")
async def edit_api_key(api_key: ApiTokenEdit = Body(..., example={'token': 'your_api_token', 'status': 'inactive'})):
    """
    Edit the status of an api key.
    """ 
    try:
        change_api_key_status(api_key.token, api_key.status)
        return {"message": "API key status updated successfully"}
    except:
        raise HTTPException(status_code=400, detail="Failed to update API key status")



@router.delete("/{key}")
async def delete_inactive_api_key(key: str):
    """
    Delete an api key with a status of inactive.
    """
    api_key = settings.API_COLL.find_one({"api_key": key})
    if api_key and api_key['status'] == "inactive":
        await delete_api_key(api_key['user'], key)
        return {"message": "API key deleted"}
    else:
        raise HTTPException(status_code=400, detail="Cannot delete active api key")

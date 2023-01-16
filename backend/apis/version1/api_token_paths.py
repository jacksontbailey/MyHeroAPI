from fastapi import APIRouter, Body, HTTPException
from schemas.schema_token import ApiTokenCreate, ApiTokenEdit
from db.repository.token import save_api_key, change_api_key_status, add_api_keys, delete_api_key
from core.security_funct import generate_token
from core.config import settings


router = APIRouter()


@router.post("/create", response_model=ApiTokenCreate)
async def create_api_token(token: ApiTokenCreate):
    """
    Create a new api token.
    """
    new_token = generate_token()
    save_api_key(token.user, new_token, token.expires, token.status, token.time_limit)
    add_api_keys(token.user, new_token)
    return {"token": new_token}



@router.get("/list/{user}")
async def list_api_tokens(user: str):
    """
    List all the api keys for a user.
    """
    user_data = settings.USER_COLL.find_one({"user": user})
    if not user_data or "api_keys" not in user_data:
        raise HTTPException(status_code=404, detail="API keys not found for this account.")
    api_keys = list(user_data.get("api_keys"))
    return api_keys



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



@router.delete("/{token}")
async def delete_inactive_api_key(token: str):
    """
    Delete an api key with a status of inactive.
    """
    api_key = settings.API_COLL.find_one({"token": token})
    if api_key and api_key['status'] == "inactive":
        await delete_api_key(api_key['user'], token)
        return {"message": "API key deleted"}
    else:
        raise HTTPException(status_code=400, detail="Cannot delete active api key")

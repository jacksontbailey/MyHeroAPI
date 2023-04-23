import useSWR from 'swr';

class User {
  constructor(userData) {
    // Destructure the user data and assign it to class properties
    const { username, email, is_active, is_superuser, is_verified } = userData;
    this.username = username;
    this.email = email;
    this.isActive = is_active;
    this.isSuperuser = is_superuser;
    this.isVerified = is_verified;
    // Initialize the API keys as an empty array
    this.apiKeys = [];
    this.authToken = null
  }

  async loadKeys() {
    // Fetch the API keys from the backend and assign them to the class property
    const { data: keysData, error: keysError } = useSWR(`${process.env.NEXT_PUBLIC_API_URL}/api_keys/list-keys`, async url => {
      const response = await fetch(url);
      const data = await response.json();
      if (Array.isArray(data)) {
        return data;
      }
    });
    if (keysError) {
      console.log(keysError);
    }
    if (Array.isArray(keysData)) {
      this.apiKeys = keysData;
    }
  }

  hasKey(apiKey) {
    // Check if the user has a specific API key
    return this.authToken.some(key => key.token === apiKey);
  }

  async removeKey(apiKey) {
    // Remove a specific API key from the user's list
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api_keys/remove-key`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({ username: this.username }),
    });
    if (response.ok) {
      // If the API key was removed successfully, update the API keys using mutate
      mutate(`${process.env.NEXT_PUBLIC_API_URL}/api_keys/list-keys`);
    }
  }
  
  async deleteKey(key) {
    try {
      const token = this.authToken;
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api_keys/delete-key?key=${key}`, {
          method: "DELETE",
          headers: {
              'Authorization': `Bearer ${token}`,
          }
      })
      if (res.ok) {
        // If the API key was deleted successfully, update the API keys array
        this.apiKeys = this.apiKeys.filter(apiKey => apiKey.key !== key);
      }
      return res.status
    } catch (error) {
      return error
    }
  }

  async updateKey({currentKey, updateStatus = null, updateName = null}) {
    try {
      const token = this.authToken;
      let url = `${process.env.NEXT_PUBLIC_API_URL}/api_keys/edit-key?key=${currentKey}`;
      if (updateStatus) {
          url += `&status=${updateStatus}`;
      }
      if (updateName) {
          url += `&name=${updateName}`;
      }
      const res = await fetch(url, {
          method:"PATCH",
          headers: {
              'Authorization': `Bearer ${token}`,
          }
      })
      if (res.ok) {
        // If the API key was updated successfully, update the API keys array
        const updatedKey = await res.json();
        const keyIndex = this.apiKeys.findIndex(apiKey => apiKey.key === currentKey);
        if (keyIndex !== -1) {
          this.apiKeys[keyIndex] = updatedKey;
        }
      }
      return res.status
    } catch (error) {
        return error
    }}
}

export default User;

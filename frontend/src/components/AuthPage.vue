<template>
  <div class="auth-container">
    <LoginContent @userLogin="userLogin"></LoginContent>
  </div>
</template>

<script>
import LoginContent from "@/components/LoginContent";

export default {
  name: 'AuthPage',
  components: {LoginContent},
  data() {
    return {
      loginDetails: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    userLogin(credentials) {
      const loginOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(credentials)
      }
      fetch('/api/v1/users/token', loginOptions).then(response => response.json()).then(data => localStorage.token = data.access_token)
    },
  }
}
</script>

<style>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}


label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button[type="submit"] {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #0056b3;
}
</style>
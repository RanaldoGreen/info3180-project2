<template>
  <div>
    <h1>Login</h1>
    <form id="LoginForm" @submit.prevent="loginUser">
      <div v-if="success" class="alert alert-success">
        User login successful
      </div>
      <div v-if="errors.length" class="alert alert-danger">
        <ul>
          <li v-for="error in errors">{{ error }}</li>
        </ul>
      </div>
      <div class="form-group mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" name="username" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" name="password" class="form-control"/>
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let success = ref(false);

let csrf_token = ref("");
let errors = ref([]);
let errorDisplayStatus = ref({});

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      csrf_token.value = data.csrf_token;
  })
}

onMounted(() => {
  getCsrfToken();
});

function validateForm() {
  errors.value = [];
  errorDisplayStatus.value = {};

  let usernameInput = document.getElementsByName("username")[0];
  let passwordInput = document.getElementsByName("password")[0];

  if (!usernameInput.value) {
    errors.value.push("Username is required");
  }

  if (!passwordInput.value) {
    errors.value.push("Password is required");
  }

  // Set errorDisplayStatus to false for each error that has not been displayed yet
  errors.value.forEach(error => {
    if (!errorDisplayStatus.value[error]) {
      errorDisplayStatus.value[error] = false;
    }
  });

  if (errors.value.length > 0) {
    // Scroll to the top of the page to show the error messages
    window.scrollTo(0, 0);
  }

  return errors.value.length === 0;
}

function loginUser() {
  let LoginForm = document.getElementById('LoginForm');
  let form_data = new FormData(LoginForm);

  if (validateForm()) {
    fetch("/api/v1/auth/login", {
      method: 'POST',
      body: form_data,
      headers: {
        'X-CSRFToken': csrf_token.value
      }
    })
      .then(function (response) {
        if (response.ok) {
          success.value = true;
        } else {
          return response.json();
        }
      })
      .then(function (data) {
        if (data.error) {
          errors.value.push(data.error);
        } else {
          console.log(data.message);
        }
      })
      .catch(function (error) {
        console.log(error);
        errors.value.push(error.response.data.error);
      });
  }
}
</script>


<style>
#LoginForm{
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

h1{
  max-width: 500px;
  margin: 0 auto;
  padding-bottom: 20px;
}
</style>
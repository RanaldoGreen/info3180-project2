<template>
    <div>
      <h1>New Post</h1>
      <form id="PostForm" @submit.prevent="savePost">
        <div v-if="success" class="alert alert-success">
          Post successful
        </div>
        <div v-if="errors.length" class="alert alert-danger">
          <ul>
            <li v-for="error in errors">{{ error }}</li>
          </ul>
        </div>
        <div class="form-group mb-3">
            <label for="photo" class="form-label">Photo</label>
            <input type="file" name="photo" class="form-control" />
        </div>
        <div class="form-group mb-3">
            <label for="caption" class="form-label">Caption</label>
            <textarea name="caption" class="form-control"></textarea>
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
  
    let photoInput = document.getElementsByName("photo")[0];
    let captionInput = document.getElementsByName("caption")[0];
  
    if (!photoInput.value) {
      errors.value.push("Photo is required");
    }
  
    if (!captionInput.value) {
      errors.value.push("Caption is required");
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
  
  function savePost() {
    let PostForm = document.getElementById('PostForm');
    let form_data = new FormData(PostForm);
  
    if (validateForm()) {
      fetch("/api/v1/users/2/posts", {
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
  #PostForm{
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
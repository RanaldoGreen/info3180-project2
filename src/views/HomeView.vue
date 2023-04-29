<script setup>
import { ref } from "vue";
import { RouterLink } from "vue-router";

let message = ref("Hello World! This is a VueJS and Flask Starter Template.")

</script>

<template>
  <div class="back">
    <div class="container">
      <div class="left">
        <img src="https://cdn.wallpapersafari.com/3/10/wd0At9.jpg" alt="">
      </div>
      <div class="right">
        <div class="card">
          <div class="logo">
            <img class="i" src="camera.png" alt="">
            <h2>Photogram</h2>
          </div>
          <hr>
          <div class="text">
            Share photos of your favourite moments with friends, family and the world.
          </div>
          <div class="button">
            <RouterLink id="reg" class="link" to="/register">Register</RouterLink>
            <RouterLink id="log" class="link" to="/login">Login</RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.back {
  background-image: url("https://wallpaperaccess.com/full/3082467.jpg");
  background-size: cover;
  background-position: top;
  width: 100%;
  margin-top: -70px; /* Adjust the negative margin value to remove the space */
}

.container {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.left {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 400px;
  height: 300px; /* Set a fixed height for the photo card */
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
  overflow: hidden;
  border-radius: 10px;
}

.left > img {
  width: 100%;
  height: 100%; /* Make the image fill the entire container */
  object-fit: cover; /* Maintain aspect ratio and cover the container */
}

.right {
  display: flex;
  align-items: center;
}

.card {
  display: flex;
  flex-direction: column;
  width: 400px;
  height: 300px;
  align-items: center;
  justify-content: flex-start;
  gap: 10px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
  background-image: url("https://www.wallpapers.net/spot-light-background-hd-wallpaper/download/3840x2160.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.card > .logo > img {
  object-fit: contain;
  width: 28px;
}

.logo {
  display: flex;
  margin-top: 10px;
  align-items: center;
  gap: 5px
}

.text {
  margin: 0 10px;
  text-align: left;
  padding-bottom: 10px;
}

hr {
  width: 90%;
}

.button {
  margin-top: 30px;
  width: 80%;
  display: flex;
  gap: 10px;
  text-align: center;
}

.button .link {
  flex: 1;
  text-decoration: none;
  color: #fff;
  background: rgb(50, 147, 177);
  padding: 10px;
}

#reg {
  background-color: rgb(0, 145, 255);
}

#log {
  background-color: black;
}

.i {
  width: 100%;
}
</style>

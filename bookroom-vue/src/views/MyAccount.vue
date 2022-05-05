<template>
  <div>
    <h1>My Account</h1>
    <br />
    <div><button @click="logout()" class="btn btn-danger">Log out</button></div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MyAccount",
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");

      this.$store.commit("removeToken");

      this.$router.push("/");
    },
  },
};
</script>

<style></style>

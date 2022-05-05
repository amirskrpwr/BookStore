<template>
  <div>
    <div class="d-flex justify-content-center"><h1>Sign Up</h1></div>
    <br />
    <div class="d-flex justify-content-center">
      <form @submit.prevent="submitForm" class="width">
        <div class="form-field">
          <input
            type="text"
            name="username"
            id=""
            placeholder="Username"
            v-model="username"
            class="form-control"
          />
          <br />
          <input
            type="password"
            name="password"
            id=""
            placeholder="Password"
            v-model="password"
            class="form-control"
          />
          <br />
          <input
            type="password"
            name="password2"
            id=""
            placeholder="Password again"
            v-model="password2"
            class="form-control"
          />
          <br />
          <div class="" v-if="errors.length">
            <p v-for="error in errors" :key="error.id">{{ error }}</p>
          </div>
          <div class="d-grid gap-2">
            <button class="btn btn-primary">Sign Up</button>
          </div>
        </div>
        <hr />
        Or <router-link to="/log-in">click here</router-link> to Log in!
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      errors: [],
    };
  },
  methods: {
    submitForm() {
      this.errors = [];

      if (this.username === "") {
        this.errors.push("The username is missing");
      }
      if (this.password === "") {
        this.errors.push("The password is too short");
      }
      if (this.password !== this.password2) {
        this.errors.push("The passwords are not matched");
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
        };

        axios
          .post("api/v1/users/", formData)
          .then((res) => {
            console.log(res);
            this.$router.push("/log-in");
          })
          .catch((err) => {
            if (err.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}:${err.response.data[property]}`);
              }

              console.log(JSON.stringify(error.response.data));
            } else if (err.message) {
              this.errors.push("Something went wrong. Please try again.");

              console.log(JSON.stringify(err));
            }
          });
      }
    },
  },
};
</script>

<style scoped>
.width {
  width: 420px;
}
</style>

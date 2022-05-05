<template>
  <div>
    <div class="d-flex justify-content-center"><h1>Log In</h1></div>
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

          <div class="p-3 mb-2 bg-danger text-white" v-if="errors.length">
            <p v-for="error in errors" :key="error.id">{{ error }}</p>
          </div>
          <div class="d-grid gap-2">
            <button class="btn btn-primary">Log In</button>
          </div>
        </div>
        <hr />
        Or <router-link to="/sign-up">click here</router-link> to sign up!
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
      // email:
    };
  },

  mounted() {
    document.title = "Login | BookRoom";
  },

  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");

      const formData = {
        username: this.username,
        password: this.password,
      };

      await axios
        .post("api/v1/token/login/", formData)
        .then((res) => {
          const token = res.data.auth_token;
          axios.defaults.headers.common["Authorization"] = "Token " + token;
          this.$store.commit("setToken", token);
          this.$store.commit("setUsername", formData.username);
          this.$store.commit("setPassword", formData.password);
          localStorage.setItem("token", token);
          localStorage.setItem("username", formData.username);
          localStorage.setItem("password", formData.password);
          const toPath = this.$route.query.to || "/cart";

          this.$router.push(toPath);
        })
        .catch((err) => {
          if (err.response) {
            for (const property in err.response.data) {
              this.errors.push(`${property}: ${err.response.data[property]}`);
            }
            console.log(JSON.stringify(err.response.data));
          } else if (err.message) {
            this.errors.push("Something went wrong. Please try again");
            console.log(JSON.stringify(err));
          }
        });
    },
  },
};
</script>
<style scoped>
.width {
  width: 420px;
}
</style>

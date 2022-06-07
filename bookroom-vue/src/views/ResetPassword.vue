<template>
  <div>
    <div class="login-form-container">
      <form action="" @submit.prevent="forgotPassword">
        <h3>بازیابی رمز عبور</h3>
        <span>آدرس ایمیل</span>
        <input
          type="email"
          name="email"
          id="email"
          v-model="email"
          class="form-control box"
          placeholder="نام کاربری خود را وارد کنید"
        />
        <input type="submit" value="ارسال ایمیل" class="btn" />
        <div class="p-3 mb-2 bg-danger text-white" v-if="errors.length">
          <p v-for="error in errors" :key="error.id">{{ error }}</p>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ResetPassword",
  data() {
    return {
      email: "",
      errors: [],
    };
  },

  mounted() {
    document.title = "ResetPassword | BookRoom";
  },

  methods: {
    async forgotPassword() {
      await axios
        .post("api/v1/users/reset_password/", {
          email: this.email,
        })
        .then((res) => {
          console.log("email sent to ", this.email);

          Toastify({
            text: "ایمیل به آدرس " + this.email + " فرستاده شد",
            duration: 3000,
            newWindow: true,
            gravity: "bottom",
            position: "right",
            stopOnFocus: true,
            style: {
              background: "#5cdb95",
            },
          }).showToast();

          this.$router.push("/");
        })
        .catch((err) => {
          console.log(err);

          Toastify({
            text: "مشکلی پیش آمد. دوباره تلاش کنید.",
            duration: 3000,
            newWindow: true,
            gravity: "bottom",
            position: "right",
            stopOnFocus: true,
            style: {
              background: "#ff652f",
            },
          }).showToast();
        });

      this.$router.push("/log-in");
    },
  },
};
</script>
<style scoped>
.width {
  width: 420px;
}

.box {
  margin: 2rem 0;
  position: relative;
  overflow: hidden;
  border: var(--border);
  text-align: center;
}

.box:hover {
  border: var(--border-hover);
}

.btn {
  margin-top: 1rem;
  display: inline-block;
  padding: 0.9rem 3rem;
  border-radius: 0.5rem;
  color: #fff;
  background: var(--green);
  font-size: 1.3rem;
  cursor: pointer;
  font-weight: 500;
}

.btn:hover {
  background: var(--dark-color);
}

.login-form-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  width: 100%;
}

.login-form-container form {
  background: #fff;
  border: var(--border);
  width: 35rem;
  padding: 1.6rem;
  box-shadow: var(--box-shadow);
  border-radius: 0.5rem;
  margin: 1.7rem;
}

.login-form-container form h3 {
  font-size: 2rem;
  text-transform: uppercase;
  color: var(--black);
  text-align: center;
}

.login-form-container form span {
  display: block;
  font-size: 1.2rem;
  padding-top: 0.8rem;
}

.login-form-container form .box {
  width: 100%;
  margin: 0.7rem 0;
  font-size: 1rem;
  border: var(--border);
  border-radius: 0.5rem;
  padding: 0.8rem 1rem;
  color: var(--black);
  text-transform: none;
}

.login-form-container form .checkbox {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 0;
}

.login-form-container form .checkbox label {
  font-size: 1rem;
  color: var(--light-color);
  cursor: pointer;
}

.login-form-container form .btn {
  text-align: center;
  width: 100%;
  margin: 1.2rem 0;
}

.login-form-container form p {
  padding-top: 0.8rem;
  color: var(--light-color);
  font-size: 1rem;
}

.login-form-container form p a {
  color: var(--green);
  text-decoration: underline;
}
</style>

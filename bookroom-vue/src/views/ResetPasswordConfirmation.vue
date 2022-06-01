<template>
  <div>
    <div class="login-form-container">
      <form action="" @submit.prevent="resetPassword">
        <h3>بازیابی رمز عبور</h3>
        <span>رمز عبود جدید</span>
        <input
          type="password"
          name="password"
          id="password"
          v-model="password"
          class="form-control box"
          placeholder="رمز عبور جدید خود را وارد کنید"
        />
        <input type="submit" value="ثبت رمز عبور" class="btn" />
        <div class="p-3 mb-2 bg-danger text-white" v-if="errors.length">
          <p v-for="error in errors" :key="error.id">{{ error }}</p>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import Toastify from "toastify-js";
import axios from "axios";

export default {
  name: "ResetPasswordConfirmation",
  data() {
    return {
      password: "",
      uid: this.$route.params.uid,
      token: this.$route.params.token,
      errors: [],
    };
  },

  methods: {
    async resetPassword() {
      await axios
        .post("/api/v1/users/reset_password_confirm/", {
          uid: this.uid,
          token: this.token,
          new_password: this.password,
        })
        .then((res) => {
          console.log("email successfully changed.");

          Toastify({
            text: "رمز عبور با موفقیت تغییر کرد.",
            duration: 3000,
            newWindow: true,
            gravity: "bottom",
            position: "right",
            stopOnFocus: true,
            style: {
              background: "#5cdb95",
            },
          }).showToast();

          this.$router.push("/log-in");
        })
        .catch((err) => {
          console.log(err);

          Toastify({
            text: "متاسفانه ایمیل تغییر پیدا نکرد . لطفا دوباره امتحان کنید.",
            duration: 3000,
            newWindow: true,
            gravity: "bottom",
            position: "right",
            stopOnFocus: true,
            style: {
              background: "#ff652f",
            },
          }).showToast();

          this.$router.push("/log-in");
        });
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

<template>
  <div>
    <div class="login-form-container">
      <form action="" @submit.prevent="submitForm">
        <h3>ثبت نام</h3>
        <span>نام کاربری</span>
        <input
          type="text"
          name="username"
          id="username"
          v-model="username"
          class="form-control box"
          placeholder="نام کاربری خود را وارد کنید"
        />
        <span>رمز عبور</span>
        <input
          type="password"
          name="password"
          id="password"
          v-model="password"
          class="form-control box"
          placeholder="رمز عبور خود را وارد کنید"
        />
        <input
          type="password"
          name="password2"
          id="password"
          v-model="password2"
          class="form-control box"
          placeholder="رمز عبور خود را مجدداً وارد کنید"
        />
        <input type="submit" value="ساخت حساب" class="btn" />
        <p>حساب دارید؟ <router-link to="/log-in">ورود به حساب</router-link></p>
      </form>
    </div>
  </div>
</template>

<script>
import Toastify from "toastify-js";
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
        this.errors.push("نام کاربری وارد نشده است");
        Toastify({
          text: "نام کاربری وارد نشده است",
          duration: 3000,
          newWindow: true,
          gravity: "bottom",
          position: "right",
          stopOnFocus: true,
          style: {
            background: "#ff652f",
          },
        }).showToast();
      }
      if (this.password === "") {
        this.errors.push("رمزعبور وارد نشده‌است");
        Toastify({
          text: "رمزعبور وارد نشده‌است",
          duration: 3000,
          newWindow: true,
          gravity: "bottom",
          position: "right",
          stopOnFocus: true,
          style: {
            background: "#ff652f",
          },
        }).showToast();
      }
      if (this.password.length < 8) {
        this.errors.push("رمزعبور باید حداقل شامل 8 کاراکتر باشد");
        Toastify({
          text: "رمزعبور باید حداقل شامل 8 کاراکتر باشد",
          duration: 3000,
          newWindow: true,
          gravity: "bottom",
          position: "right",
          stopOnFocus: true,
          style: {
            background: "#ff652f",
          },
        }).showToast();
      }
      if (this.password !== this.password2) {
        this.errors.push("رمزهای عبور با هم تطابق ندارند");
        Toastify({
          text: "رمزهای عبور با هم تطابق ندارند",
          duration: 3000,
          newWindow: true,
          gravity: "bottom",
          position: "right",
          stopOnFocus: true,
          style: {
            background: "#ff652f",
          },
        }).showToast();
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

            Toastify({
              text: "ثبت نام با موفقیت انجام شد. لطفا وارد شوید.",
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
            if (err.response) {
              for (const property in err.response.data) {
                this.errors.push(`${property}:${err.response.data[property]}`);

                Toastify({
                  text: `${property}:${err.response.data[property]}`,
                  duration: 3000,
                  newWindow: true,
                  gravity: "bottom",
                  position: "right",
                  stopOnFocus: true,
                  style: {
                    background: "#ff652f",
                  },
                }).showToast();
              }

              console.log(JSON.stringify(error.response.data));
            } else if (err.message) {
              this.errors.push("مشکلی رخ داده‌است. لطفا دوباره امتحان کنید.");

              Toastify({
                text: "مشکلی رخ داده‌است. لطفا دوباره امتحان کنید.",
                duration: 3000,
                newWindow: true,
                gravity: "bottom",
                position: "right",
                stopOnFocus: true,
                style: {
                  background: "#ff652f",
                },
              }).showToast();

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

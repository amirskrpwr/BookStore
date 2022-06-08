import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import Vue3PersianDatetimePicker from "vue3-persian-datetime-picker";

axios.defaults.baseURL = "https://bookroom-backend.herokuapp.com";

createApp(App)
    .use(Vue3PersianDatetimePicker, {
        name: "BirthDatePicker",
        props: {
            format: "YYYY-MM-DD",
            displayFormat: "jYYYY-jMM-jDD",
            editable: false,
            inputClass: "form-control",
            placeholder: "لطفا تاریخ تولد خود را مشخص کنید.",
            altFormat: "YYYY-MM-DD HH:mm",
            color: "#5cdb95",
            autoSubmit: false,
            //...
            //... And whatever you want to set as default.
            //...
        },
    })
    .use(store)
    .use(router, axios)
    .mount("#app");
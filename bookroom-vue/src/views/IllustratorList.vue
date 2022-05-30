<template>
  <div>
    <h2 v-if="!$store.state.isLoading">نویسندگان</h2>
    <hr />
    <br />
    <div class="row">
      <div
        v-for="illustrator in illustratorList"
        :key="illustrator.id"
        class="col-lg-3 col-md-6 mb-3"
      >
        <div class="box-element">
          <router-link
            v-bind:to="illustrator.get_absolute_url"
            class="text-decoration-none text-black-50"
          >
            <div
              v-if="illustrator.get_image"
              class="d-flex justify-content-center"
            >
              <img
                v-if="illustrator.get_image"
                class="thumbnail"
                :src="illustrator.get_image"
                :alt="illustrator.name"
              />
            </div>
            <div v-else class="d-flex justify-content-center">
              <img
                src="../assets/images/default.png"
                class="thumbnail"
                alt="default"
              />
            </div>
            <h6 class="mt-3 p-2">
              {{ illustrator.name }}
            </h6>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "illustratorList",
  data() {
    return {
      illustratorList: [],
    };
  },
  mounted() {
    document.title = "illustrators | BookRoom";
    this.getillustrators();
  },
  methods: {
    async getillustrators() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("api/v1/illustrator_list/")
        .then((res) => {
          this.illustratorList = res.data;
          console.log(this.illustratorList);
        })
        .catch((err) => console.log(err));

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>

<style scoped>
.thumbnail {
  width: 65%;
  height: 150px;
}

.box-element {
  box-shadow: hsl(0, 0%, 80%) 0 0 16px;
  background-color: #fff;
  border-radius: 4px;
  padding: 10px;
}
</style>

<template>
  <div>
    <h2 v-if="!$store.state.isLoading">publishers</h2>
    <br />
    <div class="row">
      <div
        v-for="publisher in publisherList"
        :key="publisher.id"
        class="col-lg-3 col-md-6 mb-3"
      >
        <div class="box-element">
          <router-link
            v-bind:to="publisher.get_absolute_url"
            class="text-decoration-none text-black-50"
          >
            <div
              v-if="publisher.get_image"
              class="d-flex justify-content-center"
            >
              <img
                v-if="publisher.get_image"
                class="thumbnail"
                :src="publisher.get_image"
                :alt="publisher.name"
              />
            </div>
            <div v-else class="d-flex justify-content-center">
              <img
                src="../assets/images/publisher.png"
                class="thumbnail"
                alt="default"
              />
            </div>
            <h6 class="mt-3 p-2">
              {{ publisher.name }}
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
  name: "PublisherList",
  data() {
    return {
      publisherList: [],
    };
  },
  mounted() {
    document.title = "Publishers | BookRoom";
    this.getPublishers();
  },
  methods: {
    async getPublishers() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("api/v1/publisher_list/")
        .then((res) => {
          this.publisherList = res.data;
          console.log(this.publisherList);
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

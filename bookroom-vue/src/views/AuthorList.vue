<template>
  <div>
    <h2 v-if="!$store.state.isLoading">Authors</h2>
    <br />
    <div class="row">
      <div
        v-for="author in authorList"
        :key="author.id"
        class="col-lg-3 col-md-6 mb-3"
      >
        <div class="box-element">
          <router-link
            v-bind:to="author.get_absolute_url"
            class="text-decoration-none text-black-50"
          >
            <div v-if="author.get_image" class="d-flex justify-content-center">
              <img
                v-if="author.get_image"
                class="thumbnail"
                :src="author.get_image"
                :alt="author.name"
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
              {{ author.name }}
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
  name: "AuthorList",
  data() {
    return {
      authorList: [],
    };
  },
  mounted() {
    document.title = "Authors | BookRoom";
    this.getAuthors();
  },
  methods: {
    async getAuthors() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("api/v1/author_list/")
        .then((res) => {
          this.authorList = res.data;
          console.log(this.authorList);
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

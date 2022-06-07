<template>
  <div>
    <h2>{{ publisher.name }}</h2>
    <br />
    <div class="row">
      <div class="col-lg-3 col-md-6 mb-3">
        <img
          v-if="publisher.get_image"
          :src="publisher.get_image"
          class="img-thumbnail"
          width="230"
          :alt="publisher.name"
        />
        <img
          v-else
          src="../assets/images/publisher.png"
          class="img-thumbnail"
          width="230"
          :alt="publisher.name"
        />
      </div>
      <div class="col-lg-9 col-md-6 mb-3">
        <div v-if="publisher.introduction">
          <p>{{ publisher.introduction }}</p>
          <br /><br />
        </div>
      </div>
    </div>
    <br />
    <br />
    <div class="row">
      <h2>کتاب‌ها</h2>
      <hr />
      <BookBox
        v-for="book in publisher.books"
        :key="book.id"
        v-bind:book="book"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import BookBox from "@/components/BookBox.vue";

export default {
  name: "publisher",
  data() {
    return {
      publisher: {},
    };
  },
  mounted() {
    this.getPublisher();
  },
  methods: {
    async getPublisher() {
      this.$store.commit("setIsLoading", true);

      const publisher_slug = this.$route.params.publisher_slug;
      await axios
        .get(`/api/v1/publishers/${publisher_slug}/`)
        .then((res) => {
          this.publisher = res.data;
          document.title = this.publisher.name + " | BookRoom";
        })
        .catch((err) => console.log(err));

      this.$store.commit("setIsLoading", false);
    },
  },
  components: {
    BookBox,
  },
};
</script>

<style scoped></style>

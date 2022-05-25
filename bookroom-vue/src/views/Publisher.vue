<template>
  <div>
    <h2>{{ publisher.name }}</h2>
    <br />
    <img
      v-if="publisher.get_image"
      :src="publisher.get_image"
      class="img-thumbnail"
      width="200"
      height="150"
      :alt="publisher.name"
    />
    <img
      v-else
      src="../assets/images/publisher.png"
      class="img-thumbnail"
      width="200"
      height="150"
      :alt="publisher.name"
    />
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

<style></style>

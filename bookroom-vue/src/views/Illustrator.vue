<template>
  <div>
    <h2>{{ illustrator.name }}</h2>
    <br />
    <div class="row">
      <div class="col-lg-3 col-md-6 mb-3">
        <img
          v-if="illustrator.get_image"
          :src="illustrator.get_image"
          class="img-thumbnail"
          width="200"
          height="150"
          :alt="illustrator.name"
        />
        <img
          v-else
          src="../assets/images/default.png"
          class="img-thumbnail"
          width="230"
          :alt="illustrator.name"
        />
        <div v-if="illustrator.birth_date">
          <br />
          <div>تاریخ تولد: {{ illustrator.birth_date }}</div>
        </div>
        <div v-if="illustrator.birth_place">
          <br />
          <div>محل تولد: {{ illustrator.birth_place }}</div>
        </div>
      </div>
      <div class="col-lg-9 col-md-6 mb-3">
        <div v-if="illustrator.introduction">
          <p>{{ illustrator.introduction }}</p>
          <br /><br />
        </div>
      </div>
    </div>
    <br />
    <br />

    <div v-show="books.length" class="row">
      <h2>کتاب‌ها</h2>
      <hr />
      <BookBox v-for="book in books" :key="book.id" v-bind:book="book" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import BookBox from "@/components/BookBox.vue";

export default {
  name: "illustrator",
  data() {
    return {
      illustrator: {},
      books: [],
    };
  },
  mounted() {
    this.getIllustrator();
  },
  methods: {
    async getIllustrator() {
      this.$store.commit("setIsLoading", true);

      const illustrator_slug = this.$route.params.illustrator_slug;
      await axios
        .get(`/api/v1/illustrators/${illustrator_slug}/`)
        .then((res) => {
          this.illustrator = res.data;
          this.books = this.illustrator.books;
          document.title = this.illustrator.name + " | BookRoom";
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

<template>
  <div>
    <h2><img :src="author.get_flag" height="20" alt="" /> {{ author.name }}</h2>
    <br />
    <div class="row">
      <div class="col-lg-3 col-md-6 mb-3">
        <img
          v-if="author.get_image"
          :src="author.get_image"
          class="img-thumbnail"
          width="200"
          height="150"
          :alt="author.name"
        />
        <img
          v-else
          src="../assets/images/default.png"
          class="img-thumbnail"
          width="230"
          :alt="author.name"
        />
        <div v-if="author.birth_date">
          <br />
          <div>
            تاریخ تولد:
            {{ toFarsiNumber(dateOfBirth) }}
          </div>
        </div>
        <div v-if="author.birth_place">
          <br />
          <div>محل تولد: {{ author.birth_place }}</div>
        </div>
      </div>
      <div class="col-lg-9 col-md-6 mb-3">
        <div v-if="author.introduction">
          <p>{{ author.introduction }}</p>
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
    <div v-show="translations.length" class="row">
      <h2>ترجمه‌ها</h2>
      <hr />
      <BookBox v-for="book in translations" :key="book.id" v-bind:book="book" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import BookBox from "@/components/BookBox.vue";

export default {
  name: "Author",
  data() {
    return {
      author: {},
      books: [],
      translations: [],
    };
  },
  mounted() {
    this.getAuthor();
  },
  computed: {
    dateOfBirth() {
      return moment(String(this.author.birth_date)).format("YYYY/MM/DD");
    },
  },
  methods: {
    async getAuthor() {
      this.$store.commit("setIsLoading", true);

      const author_slug = this.$route.params.author_slug;
      await axios
        .get(`/api/v1/authors/${author_slug}/`)
        .then((res) => {
          this.author = res.data;
          this.books = this.author.books;
          this.translations = this.author.translations;
          document.title = this.author.name + " | BookRoom";
        })
        .catch((err) => console.log(err));

      this.$store.commit("setIsLoading", false);
    },
    toFarsiNumber(n) {
      const farsiDigits = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"];
      return n.toString().replace(/\d/g, (x) => farsiDigits[x]);
    },
  },
  components: {
    BookBox,
  },
};
</script>

<style scoped>
.short {
  max-width: 250px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>

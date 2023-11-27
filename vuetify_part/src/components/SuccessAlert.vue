<template>
    <v-snackbar
      :timeout="4100"
      color="success"
      transition="slide-x-reverse-transition"
      min-width="700px"
      min-height="100px"
      location="right bottom"
      class="my-10"
    >
      <v-alert
        prominent=""
        min-width="500px"
        min-height="100px"
        title="Заказ успешно оформлен!"
        type="success"
      >
        My text is here!
        <v-progress-linear
          style="position: absolute; top: 0"
          v-model="time"
        ></v-progress-linear>
      </v-alert>
    </v-snackbar>
</template>

<script>

export default {
  props: {
    timeout: {
      default: 4100
    },
  },
  data() {
    return {
      snackbar: false,
      time: 100,
    }
  },
  mounted() {
    this.startAlert()
  },
  methods: {
    startAlert() {
      setTimeout(() => {
        this.time -= 3;
        if (this.timeout <= this.time) {
          setTimeout(() => {
            this.$emit("input", false);
            this.time = 0;
          }, 500);
        } else {
          this.startAlert()
        }
      }, 100)
    },
  },
}
</script>

<style scoped>

</style>

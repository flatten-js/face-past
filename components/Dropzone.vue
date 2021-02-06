<template>
  <vue-dropzone ref="dropzone" id="dropzone" :options="options" />
</template>

<script>
import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'

export default {
  components: {
    VueDropzone: vue2Dropzone
  },
  props: {
    options: {
      type: Object,
      default: () => ({})
    }
  },
  data() {
    return {
      dropzone: null
    }
  },
  mounted() {
    this.dropzone = this.$refs.dropzone
  },
  methods: {
    upload() {
      return new Promise(resolve => {
        this.dropzone.$on('vdropzone-success', (_, res) => resolve(res))
        this.dropzone.processQueue()
      })
    }
  }
}
</script>

<style lang="css" scoped>
</style>

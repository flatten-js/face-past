<template>
  <b-container class="p-4">
    <b-row>
      <b-col>
        <dropzone ref="dz" class="mb-2" :options="options_" />
        <b-button variant="dark" @click="submit">Run</b-button>
      </b-col>
    </b-row>

  </b-container>
</template>

<script>
import Dropzone from '~~/components/Dropzone.vue'

export default {
  data() {
    return {
      options_: {
        url: '/api/upload',
        maxFiles: 1,
        acceptedFiles: 'image/*',
        autoProcessQueue: false,
        addRemoveLinks: true
      }
    }
  },
  methods: {
    submit() {
      this.$refs.dz.upload()
      .then(res => {
        console.log(res)
      })
    }
  }
}
</script>

<style lang="css" scoped>
</style>

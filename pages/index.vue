<template>
  <b-container class="d-flex flex-column vh-100 p-4">
    <b-row class="mb-4">
      <b-col>
        <dropzone ref="dz" class="mb-2" :options="options_" />
        <b-button variant="dark" @click="submit">Run</b-button>
      </b-col>
    </b-row>

    <b-row class="flex-fill">
      <b-col>
        <canvas-editor :src="file.filename | convertImagePath" :model="model" />
      </b-col>
    </b-row>

  </b-container>
</template>

<script>
import Dropzone from '~~/components/Dropzone.vue'
import CanvasEditor from '~~/components/CanvasEditor.vue'

export default {
  filters: {
    convertImagePath(name) {
      return `/images/${name}`
    }
  },
  data() {
    return {
      options_: {
        url: '/api/upload',
        maxFiles: 1,
        acceptedFiles: 'image/*',
        autoProcessQueue: false,
        addRemoveLinks: true
      },
      file: {},
      model: {}
    }
  },
  methods: {
    submit() {
      this.$refs.dz.upload()
      .then(res => {
        this.file = res.file
        this.model = res.model
      })
    }
  }
}
</script>

<style lang="css" scoped>
</style>

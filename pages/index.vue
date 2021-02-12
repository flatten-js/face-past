<template>
  <b-container class="d-flex flex-column vh-100 p-4">
    <b-row class="mb-4">
      <b-col>
        <dropzone ref="dz" class="mb-2" :options="options_" />
        <b-button variant="dark" @click="submit">Run</b-button>
      </b-col>
    </b-row>

    <b-row class="flex-fill mb-4">
      <b-col>
        <canvas-editor
          :src="convertImagePath"
          :model="model"
          :debug="debug"
        />
      </b-col>
    </b-row>

    <b-row>
      <b-col class="text-right">
        <b-form-checkbox v-model="debug">Debug</b-form-checkbox>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Dropzone from '~~/components/Dropzone.vue'
import CanvasEditor from '~~/components/CanvasEditor.vue'

export default {
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
      model: {},
      debug: false
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
  },
  computed: {
    convertImagePath() {
      const { filename } = this.file
      return filename && `/images/${filename}`
    }
  }
}
</script>

<style lang="css" scoped>
</style>

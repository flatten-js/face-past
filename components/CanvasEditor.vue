<template>
  <canvas id="canvas-editor" class="w-100 h-100" />
</template>

<style scoped>
canvas[width] {
  width: auto !important;
}

canvas[height] {
  height: auto !important;
}
</style>

<script>
export default {
  props: {
    src: {
      type: String,
      default: ''
    },
    model: {
      type: Object,
      default: () => ({})
    }
  },
  data() {
    return {
      ctx: null,
      scale: 1,
      left: 0,
      top: 0
    }
  },
  mounted() {
    this.init()
  },
  methods: {
    init() {
      this.ctx = this.$el.getContext('2d')
      this.listener_()
    },
    listener_() {
      let timeid = null
      window.addEventListener('resize', e => {
        clearTimeout(timeid)
        timeid = setTimeout(() => {
          this.rerender()
        }, 500)
      })
    },
    rerender() {
      this.clear()
      this.load()
    },
    clear() {
      this.ctx.clearRect(0, 0, this.$el.width, this.$el.height)
      this.scale = 1
      this.left = 0
      this.top = 0
    },
    resize() {
      this.$el.width = null
      this.$el.height = null

      const parent = this.$el.parentNode
      const padding = this.utils_padding(parent)

      return {
        width: this.$el.width = parent.clientWidth - padding.width,
        height: this.$el.height = parent.clientHeight - padding.height
      }
    },
    load() {
      const { width, height } = this.resize()

      const image = new Image()

      image.addEventListener('load', e => {
        const aspect = {
          canvas: width / height,
          image: image.width / image.height
        }

        this.scale = Math.min(width / image.width, height / image.height)

        let w, h; w = h = 0

        if (aspect.image >= aspect.canvas) {
          w = width
          h = width / aspect.image
          this.top = (height - h) / 2
        } else {
          w = height * aspect.image
          h = height
          this.left = (width - w) / 2
        }

        const preset = [image, 0, 0, image.width, image.height]
        this.ctx.drawImage(...preset, this.left, this.top, w, h)

        this.setPacifier()
      })

      image.src = this.src
    },
    setPacifier() {
      const image = new Image()

      image.addEventListener('load', e => {
        this.model.result.forEach(coordinate => {
          let [left, top, width, height] = coordinate

          left = (left * this.scale) + this.left
          top = (top * this.scale) + this.top
          width *= this.scale
          height *= this.scale

          const preset = [image, 0, 0, image.width, image.height]
          this.ctx.drawImage(...preset, left, top, width, height)
        })
      })

      image.src = require('~~/assets/images/pacifier.png')
    }
  },
  watch: {
    src() {
      this.load()
    }
  }
}
</script>

<style lang="css" scoped>
</style>

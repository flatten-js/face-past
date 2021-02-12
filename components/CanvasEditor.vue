<template>
  <canvas id="canvas-editor" />
</template>

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
    },
    debug: {
      type: Boolean,
      default: false
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
  created() {
    this.$watch(
      () => [this.src, this.debug],
      () => {
        if (!this.src) return
        this.rerender()
      }
    )
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
      this.render()
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

      // ToDo: investigation to determine the cause (of)
      const spacing = 6

      return {
        width: this.$el.width = parent.clientWidth - padding.width,
        height: this.$el.height = parent.clientHeight - padding.height - spacing
      }
    },
    load(src, cb) {
      const image = new Image()
      image.addEventListener('load', e => cb(image))
      image.src = src
    },
    render() {
      const { width, height } = this.resize()

      this.load(this.src, image => {
        this.scale = Math.min(width / image.width, height / image.height)
        const aspect = {
          canvas: width / height,
          image: image.width / image.height
        }

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

        if (this.debug) {
          this.setFrame()
        } else {
          this.setPacifier()
        }
      })
    },
    setHelper_(cb) {
      this.model.result.forEach(coordinate => {
        let [left, top, width, height] = coordinate

        left = (left * this.scale) + this.left
        top = (top * this.scale) + this.top
        width *= this.scale
        height *= this.scale

        cb([left, top, width, height])
      })
    },
    setFrame() {
      this.setHelper_(coordinate => {
        this.ctx.lineWidth = 1
        this.ctx.strokeStyle = "rgb(0, 0, 255)"
        this.ctx.strokeRect(...coordinate)
      })
    },
    setPacifier() {
      this.load(require('~~/assets/images/pacifier.png'), image => {
        this.setHelper_(coordinate => {
          const preset = [image, 0, 0, image.width, image.height]
          this.ctx.drawImage(...preset, ...coordinate)
        })
      })
    }
  }
}
</script>

<style lang="css" scoped>
</style>

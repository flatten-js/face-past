import Vue from 'vue'

/*
 * Always add 'utils' as a prefix
 */

Vue.mixin({
  methods: {
    utils_padding(el) {
      const style = document.defaultView.getComputedStyle(el)
      const padding = style.padding.replace(/px/g, '').split(' ').map(Number)

      let top, right, bottom, left; top = right = bottom = left = 0

      switch(padding.length) {
        case 1:
          top = right = bottom = left = padding[0]
          break

        case 2:
          top = bottom = padding[0]
          right = left = padding[1]
          break;

        case 3:
          top = padding[0]
          right = left = padding[1]
          bottom = padding[2]
          break

        case 4:
          top = padding[0]
          right = padding[1]
          bottom = padding[2]
          left = padding[3]
          break

        default:
          break
      }

      return {
        top,
        right,
        left,
        bottom,
        width: right + left,
        height: top + bottom
      }
    }
  }
})

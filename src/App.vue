<template>
  <div id="app" class="app-container">
    <ShirtSelector @update-shirt="updateShirt" />
    <ColorSelector @update-color="updateColor" />
    <PrintSelector @update-print="updatePrint" />
    <Preview :shirt="selectedShirt" :color="selectedColor" :print="selectedPrint" />
  </div>
</template>

<script>
import ShirtSelector from './components/ShirtSelector.vue';
import ColorSelector from './components/ColorSelector.vue';
import PrintSelector from './components/PrintSelector.vue';
import Preview from './components/PreviewShirt.vue';

export default {
  components: {
    ShirtSelector,
    ColorSelector,
    PrintSelector,
    Preview
  },
  data() {
    return {
      selectedShirt: null,
      selectedColor: null,
      selectedPrint: null
    };
  },
  methods: {
    updateShirt(shirt) {
      this.selectedShirt = shirt;
    },
    updateColor(color) {
      this.selectedColor = color;
    },
    updatePrint(print) {
      this.selectedPrint = print;
    }
  }
};
</script>

<style>
.app-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  font-size: 1.5em;
  margin-bottom: 20px;
}

select {
  width: 100%;
  padding: 10px;
  font-size: 1em;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
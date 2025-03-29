<template>
    <div class="style-options">
        <div v-for="(style, index) in styles" :key="index" class="style-option" :data-style="style.name"
            @click="selectStyle(style.name)" :class="{ 'selected': selectedStyle === style.name }">
            <img :src="style.image" :alt="style.name" />
            <p>{{ style.name }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'StyleSelection',
    props: {
        styles: {
            type: Array,
            required: true
        },
        selectedStyle: {
            type: String,
            required: true
        }
    },
    methods: {
        selectStyle(style) {
            this.$emit('style-selected', style);
        }
    }
};
</script>


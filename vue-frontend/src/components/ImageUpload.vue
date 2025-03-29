<template>
    <div class="upload-area" @click="triggerFileInput" :class="{ 'dragover': isDragOver }">
        <input type="file" ref="fileInput" accept="image/*" @change="handleFileChange" style="display:none" />
        <p>Drag & drop your file here or click to upload</p>

        <div v-if="previewImage" id="preview">
            <img :src="previewImage" alt="Preview" />
        </div>
    </div>
</template>

<script>
export default {
    name: 'ImageUpload',
    data() {
        return {
            isDragOver: false,
            previewImage: null, // Store the preview image here
        };
    },
    methods: {
        triggerFileInput() {
            this.$refs.fileInput.click(); // Trigger the file input click
        },
        handleFileChange(event) {
            const file = event.target.files[0];
            if (file) {
                this.previewImage = URL.createObjectURL(file); // Show the preview
                this.$emit('file-chosen', file); // Emit the chosen file to the parent component
            }
        },
        handleDragOver(event) {
            event.preventDefault(); // Prevent the default behavior
            this.isDragOver = true; // Update the state to show the dragover style
        },
        handleDragLeave() {
            this.isDragOver = false; // Reset the drag state when leaving
        },
        handleDrop(event) {
            event.preventDefault(); // Prevent default drop behavior
            this.isDragOver = false; // Reset dragover state
            const file = event.dataTransfer.files[0]; // Get the dropped file
            if (file) {
                this.previewImage = URL.createObjectURL(file); // Show preview of the dropped file
                this.$emit('file-chosen', file); // Emit the chosen file to parent
            }
        }
    },
    mounted() {
        const uploadArea = this.$el;
        // Add event listeners for drag events
        uploadArea.addEventListener('dragover', this.handleDragOver);
        uploadArea.addEventListener('dragleave', this.handleDragLeave);
        uploadArea.addEventListener('drop', this.handleDrop); // Handle drop event
    },
    beforeDestroy() {
        const uploadArea = this.$el;
        // Remove event listeners when the component is destroyed
        uploadArea.removeEventListener('dragover', this.handleDragOver);
        uploadArea.removeEventListener('dragleave', this.handleDragLeave);
        uploadArea.removeEventListener('drop', this.handleDrop);
    }
};
</script>

<style scoped>
.upload-area {
    border: 2px dashed #ccc;
    padding: 20px;
    text-align: center;
    cursor: pointer;
    border-radius: 8px;
    transition: background-color 0.2s ease-in-out;
}

.upload-area.dragover {
    background-color: rgba(0, 255, 0, 0.1);
    border-color: #4caf50;
}

#preview img {
    max-width: 100%;
    height: auto;
    margin-top: 15px;
}
</style>

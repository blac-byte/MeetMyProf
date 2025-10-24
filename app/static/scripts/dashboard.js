//app/scripts/dashbord.js

const dropArea = document.querySelector('#drop-area');
const fileInput = document.getElementById('fileElem');
const uploadMessage = document.getElementById('uploadMessage');
const errorMsg = document.getElementById('errorMsg');
let currentPreview = null;
const MAX_SIZE_MB = 5;


fileInput.addEventListener('change', handleFiles);

['dragenter', 'dragover'].forEach(eventName => {
dropArea.addEventListener(eventName, (e) => {
    e.preventDefault();
    dropArea.classList.add('dragover');
});
});

['dragleave', 'drop'].forEach(eventName => {
dropArea.addEventListener(eventName, (e) => {
    e.preventDefault();
    dropArea.classList.remove('dragover');
});
});

dropArea.addEventListener('drop', (e) => {
const files = e.dataTransfer.files;
handleFiles({ target: { files } });
});

function handleFiles(event) {
const file = event.target.files[0];
if (!file) return;

errorMsg.textContent = '';
const validTypes = ['image/jpeg', 'image/png', 'image/gif'];
if (!validTypes.includes(file.type)) {
    errorMsg.textContent = 'Unsupported file type.';
    return;
}

if (file.size > MAX_SIZE_MB * 1024 * 1024) {
    errorMsg.textContent = 'File too large. Max size is 5MB.';
    return;
}

const reader = new FileReader();
reader.onload = (e) => {
    if (currentPreview) currentPreview.remove();
    uploadMessage.style.display = 'none';

    const img = document.createElement('img');
    img.src = e.target.result;
    img.className = 'preview-img';
    dropArea.appendChild(img);
    currentPreview = img;
};
reader.readAsDataURL(file);
}

// Sidebar hover expand/collapse
const sidebar = document.getElementById('sidebar');

sidebar.addEventListener('mouseenter', () => {
sidebar.classList.remove('collapsed');
});

sidebar.addEventListener('mouseleave', () => {
sidebar.classList.add('collapsed');
});


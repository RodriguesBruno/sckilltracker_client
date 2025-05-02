
const ignore_pattern_url = "/ignore"

// Handle dynamic modal population
document.addEventListener('click', function (event) {
    const target = event.target.closest('button');
    if (!target) return;

    if (target.classList.contains('btn-edit')) {
        const pattern = target.dataset.pattern;
        const patternId = target.dataset.pattern_id;
        document.getElementById('editPattern').value = pattern;
        document.getElementById('editPatternId').value = patternId;
    }
});

// Form submission handlers
const handleFormSubmit = (formId, url, method) => {
    document.getElementById(formId).addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const payload = Object.fromEntries(formData);

        fetch(url, {
            method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        })
            .then(response => response.ok ? response.json() : Promise.reject('Request failed'))
            .then(() => location.reload())
            .catch(error => alert(`Error: ${error}`));
    });
};

// Set up handlers for forms
handleFormSubmit('editForm', ignore_pattern_url, 'PUT');
handleFormSubmit('addForm', ignore_pattern_url, 'POST');

// Handle Delete Button Click
document.addEventListener('click', function (event) {
    const target = event.target.closest('.btn-delete');
    if (!target) return;

    // Set the pattern_id in the hidden field of the delete modal
    const patternId = target.dataset.pattern_id;
    document.getElementById('deletePatternId').value = patternId;

    const pattern = target.dataset.pattern;
    document.getElementById('deletePattern').innerHTML = pattern;
});

// Handle Delete Form Submission
document.getElementById('deleteForm').addEventListener('submit', function (event) {
    event.preventDefault();

    // Gather data from the form
    const patternId = document.getElementById('deletePatternId').value;

    const payload = {"pattern_id": patternId};

    // Send a DELETE request to the backend
    fetch(ignore_pattern_url, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Failed to delete pattern');
        }
    })
    .then(data => {
        // Optionally, refresh the table or update it dynamically
        location.reload();
    })
    .catch(error => {
        alert(`Error: ${error.message}`);
    });

    // Close the modal
    const deleteModal = bootstrap.Modal.getInstance(document.getElementById('deleteModal'));
    deleteModal.hide();
});



document.addEventListener('click', function (event) {
    const target = event.target.closest('.btn-delete');
    if (!target) return; // Exit if no delete button was clicked

    // Set the pattern_id in the hidden input field
    const patternId = target.getAttribute('data-pattern_id');
    document.getElementById('deletePatternId').value = patternId;

    // Open the delete modal
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    deleteModal.show();
});

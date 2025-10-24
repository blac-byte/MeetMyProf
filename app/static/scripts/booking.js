function handleSlotClick(cell) {
    // Only allow booking if the slot is available
    if (cell.classList.contains("booked")) {
        alert("This slot is already booked.");
        return;
    }

    const day = cell.dataset.day;
    const start = cell.dataset.start;
    const end = cell.dataset.end;

    const teacherName = document.querySelector('input[name="teacher_name"]').value;
    const department = document.querySelector('input[name="department"]').value;

    if (!confirm(`Book ${day} ${start}-${end} with ${teacherName}?`)) {
        return;
    }

    fetch("/book_slot", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            day: day,
            start: start,
            end: end,
            teacher_name: teacherName,
            department: department,
            teacher_id: "{{ teacher_id if teacher_id else 0 }}"  // optional if available
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            cell.textContent = "Booked";
            cell.classList.remove("available");
            cell.classList.add("booked");
        }
        alert(data.message);
    })
    .catch(err => console.error(err));
}
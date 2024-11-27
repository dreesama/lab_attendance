document.addEventListener('DOMContentLoaded', function() {
    // PC grid initialization
    const pcCells = document.querySelectorAll('.pc-cell');
    pcCells.forEach(cell => {
        cell.addEventListener('click', function() {
            if (this.dataset.role === 'teacher') {
                handlePCAssignment(this.dataset.pcId);
            }
        });
    });
    
    // Attendance marking
    const markAttendanceButtons = document.querySelectorAll('.mark-attendance');
    markAttendanceButtons.forEach(button => {
        button.addEventListener('click', async function() {
            const studentId = this.dataset.studentId;
            const courseId = this.dataset.courseId;
            
            try {
                const response = await fetch('/api/mark_attendance', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        student_id: studentId,
                        course_id: courseId,
                        status: 'present'
                    })
                });
                
                if (response.ok) {
                    this.textContent = 'Marked Present';
                    this.disabled = true;
                }
            } catch (error) {
                console.error('Error marking attendance:', error);
            }
        });
    });
}); 

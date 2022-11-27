function selectDepartment(answer) {
    document.getElementById('departmentSelection').classList.remove('d-none');
    document.getElementById('subjectSelection').classList.remove('d-none');
    if(answer.value == 1) {
        document.getElementById('cetDept').classList.remove('d-none');
        document.getElementById('plmbsDept').classList.add('d-none');
        document.getElementById('plmbsDept').selectedIndex = 0;
        document.getElementById('cetDeptSubject').classList.remove('d-none');
        document.getElementById('plmbsDeptSubject').classList.add('d-none');
    }
    else if (answer.value == 2) {
        document.getElementById('plmbsDept').classList.remove('d-none');
        document.getElementById('cetDept').classList.add('d-none');
        document.getElementById('cetDept').selectedIndex = 0;
        document.getElementById('cetDeptSubject').classList.add('d-none');
        document.getElementById('plmbsDeptSubject').classList.remove('d-none');
    }
};

function clearBoxes() {
    boxes = document.getElementsByName('clearValue');
    for (var i = 0; i < boxes.length; i++) {
        boxes[i].checked = false;
    }
};

var divCounter = 1;

function addDiv() {
    divCounter += 1
    html = '<div class="divSchedule" id="row' + divCounter + '">\
                <label for="">Day</label>\
                <select class="form-control" style="width:165px" name="day' + divCounter + '">\
                    <option selected disabled="true" >-----Select Day-----</option>\
                    <option>Monday</option>\
                    <option>Tueday</option>\
                    <option>Wednesday</option>\
                    <option>Thursday</option>\
                    <option>Friday</option>\
                    <option>Saturday</option>\
                </select>\
                <label for="">Start Time</label>\
                <input type="time" name="stime' + divCounter + '">\
                <br>\
                <label for="">End Time:</label>\
                <input type="time" name="etime' + divCounter + '">\
                <a href="#" id="' + divCounter + '"class="btn btn-primary" onclick="removeDiv(this)">&minus;</a>\
            </div>'
    var form = document.getElementById('row')
    form.innerHTML += html
};

function removeDiv(button) {
    let number = button.id
    let row = document.getElementById('row' + number)
    row.remove()
};
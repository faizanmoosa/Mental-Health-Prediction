function validateSelect(selectId) {
  var selectElement = document.getElementById(selectId);
  var value = selectElement.value.trim();
  function handleField(message) {
    setError(selectElement, message);
    selectElement.classList.add('input-error');
    selectElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
    return false;
  }
  if (selectId === 'age') {
    if (value === '') {
      return handleField('This field is required');
    } else if (value < 1 || value > 60) {
      return handleField('Age must be a number between 1 and 60');
    }
  } else if (value === 'select' || value === '') {
    return handleField('This field is required');
  }
  selectElement.classList.remove('input-error');
  setSuccess(selectElement);
  return true;
}

function validateForm() {
  var selectIds = [
    'time-stamp',
    'age',
    'gender',
    'country',
    'self-employed',
    'family-history',
    'work-interfere',
    'no-of-employees',
    'remote-work',
    'tech-company',
    'benefits',
    'care-options',
    'wellness-program',
    'seek-help',
    'anonymity',
    'leave',
    'mental-health-consequence',
    'phys-health-consequence',
    'coworkers',
    'supervisor',
    'mental-health-interview',
    'phys-health-interview',
    'mental-vs-physical',
    'obs-consequence',
  ];
  for (var i = 0; i < selectIds.length; i++) {
    if (!validateSelect(selectIds[i])) {
      return false;
    }
  }
  return true;
}

function toggleStateSelect() {
  var countrySelect = document.getElementById('country');
  var stateLabel = document.getElementById('state-label');
  var stateSelect = document.getElementById('state');
  var stateSpace = document.getElementById('state-space');
  if (countrySelect.value === '44') {
    stateLabel.style.display = 'block';
    stateSelect.style.display = 'block';
    stateSpace.style.display = 'block';
  } else {
    stateLabel.style.display = 'none';
    stateSelect.style.display = 'none';
    stateSpace.style.display = 'none';
  }
}

function handleCountryChange() {
  validateSelect('country');
  toggleStateSelect();
}

const setError = (element, message) => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector('.error');
  errorDisplay.innerText = message;
};

const setSuccess = (element) => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector('.error');
  errorDisplay.innerText = '';
};

function predictAgain() {
  history.back();
}

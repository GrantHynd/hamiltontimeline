createEventListeners();

/**
  * Set-up event listener for creating event button.
  */
function createEventListeners() {
    var createEventElement = document.getElementById('create-event');
    createEventElement.addEventListener('mouseup', function(e) {
        onCreateEvent(e);
    });
}

/**
  * Prevent default submit and build GraphQL Mutation string. Then submit Mutation via AJAX.
  */
function onCreateEvent(e) {
    e.preventDefault();
    var payloadVariables = getPayloadVariables();
    var formElements = e.target.form.elements;
    var title = formElements.title.value;
    var description = formElements.description.value;
    var occurredOn = formElements.occurred_on.value;
    var createEventMutation = getCreateEventMutation(payloadVariables, title, description, occurredOn);
    submit(createEventMutation);
}

/**
  * Variables that are being mutated.
  */
function getPayloadVariables() {
    return "event { title description occurredOn }"
}


/**
  * Full Mutation string.
  */
function getCreateEventMutation(payloadVariables, title, description, occurredOn) {
    return {
            "query": "mutation createEvent($event: CreateEventInput!) { createEvent(input: $event) {"+ payloadVariables +"} }",
            "operationName": "createEvent",
            "variables": {
                "event": {
                    "title": title,
                    "description": description,
                    "occurredOn": occurredOn
                }
            }
        }
}

/**
  * Submit Event Mutation string to GraphQL endpoint and either display success or error message.
  *
  * Note: Response status will be 200 even with error, handle errors via 'response.errors'.
  */
function submit(createEventMutation) {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/graphql", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onreadystatechange = function () {
        if (xhttp.readyState != 4 || xhttp.status != 200) return;
        var response = JSON.parse(xhttp.response);

        if(response.errors != null) {
            handleResponseOnError(response.errors)
        } else {
            handleResponseOnSuccess(response.data);
        }
    };
    xhttp.send(JSON.stringify(createEventMutation));
}

/**
  * Format errors for HTML and set status message.
  */
function handleResponseOnError(responseErrors) {
    formattedErrorsHTML = formatErrorsForHTML(responseErrors)
    setStatusMessage(formattedErrorsHTML);
}

/**
  * Format errors into HTML list
  */
function formatErrorsForHTML(errors) {
    var formattedErrors = '<ul>';
    for(var i=0; i < errors.length; i++) {
        formattedErrors += '<li>'+ errors[i].message +'</li>';
    }
    formattedErrors += '<ul>';
    return formattedErrors;
}

/**
  * Set status for success message.
  */
function handleResponseOnSuccess(responseData) {
    var event = responseData.createEvent.event;
    setStatusMessage("Event Created: '" + event.title + "'");
}

/**
  * Make the status element visible and set status message.
  */
function setStatusMessage(statusMessage) {
    document.getElementById('status-message').style.display = 'block';
    document.getElementById("status-message").innerHTML = statusMessage;
}
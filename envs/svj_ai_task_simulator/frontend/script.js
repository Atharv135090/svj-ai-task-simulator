// Task Config
const tasks = [
    { type: "Email Classification", content: "Email: \"Win money now!!! Click here!\"\nObjective: Classify this email as spam or not_spam", id: "email", actions: ["spam", "not_spam"] },
    { type: "Data Cleaning", content: "Input: Name = NULL\nObjective: Decide whether to clean or ignore the data", id: "data", actions: ["clean", "ignore"] },
    { type: "Code Review", content: "Code:\nprint(x)\nObjective: Identify whether the code contains a bug", id: "code", actions: ["fix_bug", "no_issue"] }
];

let currentTaskIndex = 0;

function glitchScreen() {
    document.body.classList.remove('glitch-anim');
    void document.body.offsetWidth; // Force reflow
    document.body.classList.add('glitch-anim');
}

function logTerminal(msg) {
    const term = document.getElementById('terminal-body');
    const p = document.createElement('p');
    p.innerHTML = `> ${msg}`;
    term.appendChild(p);
    term.scrollTop = term.scrollHeight;
}

function startSim() {
    glitchScreen();
    logTerminal("<span style='color:#bc13fe'>SVJ AI Core Engine Engaged...</span>");
    currentTaskIndex = 0;
    document.getElementById('terminal-body').innerHTML = '<p>> ENGINE INITIALIZED.</p>';
    renderTask();
}

function renderTask() {
    if (currentTaskIndex >= tasks.length) {
        endSim();
        return;
    }

    const task = tasks[currentTaskIndex];
    document.getElementById('task-card').classList.add('hidden');
    document.getElementById('loading').classList.remove('hidden');
    logTerminal(`Injecting System Protocol :: [${task.id.toUpperCase()}]`);

    setTimeout(() => {
        glitchScreen();
        document.getElementById('loading').classList.add('hidden');
        const card = document.getElementById('task-card');
        card.classList.remove('hidden');

        document.getElementById('task-badge').innerText = `PHASE [${currentTaskIndex + 1}/${tasks.length}]`;
        document.getElementById('task-name').innerText = task.type;
        document.getElementById('task-content').innerText = task.content;

        const actionsContainer = document.getElementById('actions-container');
        actionsContainer.innerHTML = '';
        task.actions.forEach(action => {
            const btn = document.createElement('button');
            btn.className = 'btn';
            btn.innerText = action.replace("_", " ").toUpperCase();
            btn.onclick = () => handleAction(action);
            actionsContainer.appendChild(btn);
        });

    }, 800);
}

function handleAction(action) {
    glitchScreen();
    logTerminal(`Operator Action Detected: <span style="color:#00f3ff; font-weight:bold;">${action}</span>`);
    
    document.getElementById('task-card').classList.add('hidden');

    setTimeout(() => {
        currentTaskIndex++;
        renderTask();
    }, 400);
}

function endSim() {
    const card = document.getElementById('task-card');
    card.classList.remove('hidden');

    document.getElementById('task-badge').innerText = "SEQUENCE TERMINATED";
    document.getElementById('task-name').innerText = "EVALUATION COMPLETE";
    document.getElementById('task-content').innerText = "All testing parameters handled. Matrix decoupled.";
    document.getElementById('actions-container').innerHTML = '<button class="btn" onclick="startSim()">REBOOT CORE</button>';
    
    logTerminal("<span style='color:#ff003c'>WARNING: Simulation Terminated. Aggregated scores exported.</span>");
}

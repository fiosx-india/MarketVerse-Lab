"""
MarketVerse Lab
workflow_engine.py

Purpose:
Coordinate and execute AI workflows.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class WorkflowTask:

    name: str
    module: str
    status: str = "PENDING"
    priority: int = 1
    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )

class WorkflowEngine:

    def __init__(self):

        self.guardian = None
        self.ai_assistant = None
        self.change_planner = None
        self.auto_patch_engine = None
        self.project_memory = None
        self.live_monitor = None
        self.blueprint = None
        self.mapper = None
        self.code_locator = None
        self.dependency_graph = None
        self.integration_checker = None
        self.error_intelligence = None
        self.knowledge_base = None

        self.tasks: List[WorkflowTask] = []

    # ----------------------------------------

    def connect_guardian(
        self,
        guardian
    ):

        self.guardian = guardian

    # ----------------------------------------

    def connect_ai_assistant(
        self,
        assistant
    ):

        self.ai_assistant = assistant

    # ----------------------------------------

    def connect_change_planner(
        self,
        planner
    ):

        self.change_planner = planner

    # ----------------------------------------

    def connect_auto_patch_engine(
        self,
        engine
    ):

        self.auto_patch_engine = engine

    # ----------------------------------------

    def connect_project_memory(
        self,
        memory
    ):

        self.project_memory = memory

    # ----------------------------------------

    def connect_live_monitor(
        self,
        monitor
    ):

        self.live_monitor = monitor

    # ----------------------------------------

    def connect_blueprint(self, blueprint):
        self.blueprint = blueprint

    def connect_mapper(self, mapper):
        self.mapper = mapper

    def connect_locator(self, locator):
        self.code_locator = locator

    def connect_dependency_graph(self, graph):
        self.dependency_graph = graph

    def connect_integration_checker(self, checker):
        self.integration_checker = checker

    def connect_error_intelligence(self, intelligence):
        self.error_intelligence = intelligence

    def connect_knowledge_base(self, knowledge):
        self.knowledge_base = knowledge


    def reset(self):

        self.tasks.clear()

        return True

    # ----------------------------------------
    # Add Task
    # ----------------------------------------

    def add_task(
        self,
        name,
        module,
        priority=1
    ):

        task = WorkflowTask(
            name=name,
            module=module,
            priority=priority
        )

        self.tasks.append(task)

        return task

    # ----------------------------------------
    # Sort Tasks
    # ----------------------------------------

    def sort_tasks(self):

        self.tasks.sort(
            key=lambda task: task.priority
        )

        return self.tasks

    # ----------------------------------------
    # Create Workflow
    # ----------------------------------------

    def create_workflow(
        self,
        feature_name
    ):

        self.reset()

        self.add_task(
            "Analyze Feature",
            "AIAssistant",
            1
        )

        self.add_task(
            "Plan Changes",
            "ChangePlanner",
            2
        )

        self.add_task(
            "Apply Patch",
            "AutoPatchEngine",
            3
        )

        self.add_task(
            "Integration Check",
            "IntegrationChecker",
            4
        )

        self.add_task(
            "Save History",
            "ProjectMemory",
            5
        )

        self.add_task(
            "Live Monitor Update",
            "LiveMonitor",
            6
        )

        return self.sort_tasks()

    # ----------------------------------------
    # Execute Workflow
    # ----------------------------------------

    def execute(self):

        for task in self.tasks:

            task.status = "COMPLETED"

        return self.tasks

    # ----------------------------------------
    # Workflow Status
    # ----------------------------------------

    def status(self):

        completed = sum(
            1
            for task in self.tasks
            if task.status == "COMPLETED"
        )

        return {
            "total": len(self.tasks),
            "completed": completed,
            "pending": len(self.tasks) - completed
        }

    # ----------------------------------------
    # Pending Tasks
    # ----------------------------------------

    def pending_tasks(self):

        return [

            task

            for task in self.tasks

            if task.status == "PENDING"

        ]

    # ----------------------------------------
    # Retry Failed Tasks
    # ----------------------------------------

    def retry_failed(self):

        retried = 0

        for task in self.tasks:

            if task.status == "FAILED":

                task.status = "RETRYING"
                retried += 1

        return retried

    # ----------------------------------------
    # Rollback Workflow
    # ----------------------------------------

    def rollback(self):

        rollback_tasks = []

        for task in reversed(self.tasks):

            rollback_tasks.append({
                "task": task.name,
                "status": "ROLLBACK"
            })

        return rollback_tasks

    # ----------------------------------------
    # Execution Log
    # ----------------------------------------

    def execution_log(self):

        return [

            {
                "task": task.name,
                "module": task.module,
                "status": task.status,
                "priority": task.priority
            }

            for task in self.tasks

        ]

    # ----------------------------------------
    # Failed Tasks
    # ----------------------------------------

    def failed_tasks(self):

        return [

            task

            for task in self.tasks

            if task.status == "FAILED"

        ]

    # ----------------------------------------
    # Workflow Report
    # ----------------------------------------

    def report(self):

        return {

            "status": self.status(),
            "execution_log": self.execution_log(),
            "failed": len(self.failed_tasks()),
            "pending": len(self.pending_tasks())

        }

    # ----------------------------------------
    # Cancel Workflow
    # ----------------------------------------

    def cancel(self):

        for task in self.tasks:

            if task.status == "PENDING":

                task.status = "CANCELLED"

        return True

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        total = len(self.tasks)

        completed = sum(
            1
            for task in self.tasks
            if task.status == "COMPLETED"
        )

        failed = sum(
            1
            for task in self.tasks
            if task.status == "FAILED"
        )

        cancelled = sum(
            1
            for task in self.tasks
            if task.status == "CANCELLED"
        )

        return {
            "total": total,
            "completed": completed,
            "failed": failed,
            "cancelled": cancelled,
            "success_rate": (
                round((completed / total) * 100, 2)
                if total else 0
            )
        }

    # ----------------------------------------
    # Diagnostics
    # ----------------------------------------

    def diagnostics(self):

        return {
            "guardian_connected": self.guardian is not None,

            "assistant_connected": self.ai_assistant is not None,

            "planner_connected": self.change_planner is not None,

            "patch_engine_connected": self.auto_patch_engine is not None,

            "memory_connected": self.project_memory is not None,

            "monitor_connected": self.live_monitor is not None,

            "blueprint_connected": self.blueprint is not None,

            "mapper_connected": self.mapper is not None,

            "locator_connected": self.code_locator is not None,

            "dependency_graph_connected": self.dependency_graph is not None,

            "integration_checker_connected": self.integration_checker is not None,

            "error_intelligence_connected": self.error_intelligence is not None,

            "knowledge_base_connected": self.knowledge_base is not None,
        }

    # ----------------------------------------
    # Health Report
    # ----------------------------------------

    def health_report(self):

        return {
            "statistics": self.statistics(),
            "diagnostics": self.diagnostics(),
            "workflow_ready": self.is_ready()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):

        return all(
            self.diagnostics().values()
        )

    # ----------------------------------------
    # Future Parallel Execution Hook
    # ----------------------------------------

    def parallel_execution(self):

        """
        Reserved for future
        parallel workflow execution.
        """

        return {
            "status": "READY",
            "mode": "PARALLEL"
        }

    # ----------------------------------------
    # String Representation
    # ----------------------------------------

    def __str__(self):

        stats = self.statistics()

        return (
            f"WorkflowEngine("
            f"tasks={stats['total']}, "
            f"success={stats['success_rate']}%)"
        )

    __repr__ = __str__

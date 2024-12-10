import os

def delete_projects(project_ids):
  
  for project_id in project_ids:
    try:
      # Construct the gcloud command
      command = f"gcloud projects delete {project_id} -q"  # -q for quiet mode

      # Execute the command
      print(f"Deleting project: {project_id}")
      os.system(command)

    except Exception as e:
      print(f"Error deleting project {project_id}: {e}")

if __name__ == "__main__":
  # Replace with the actual project IDs you want to delete
  projects_to_delete = ["project-id-1", "project-id-2", "project-id-3"] 

  delete_projects(projects_to_delete)

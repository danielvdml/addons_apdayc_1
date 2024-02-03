
Método 1: Cuando ya tienes un repositorio en GitHub y quieres añadir nuevos módulos
1. Clonar el repositorio con `git clone https:...`.
2. Copias los módulos en la carpeta del repositorio.
3. Agregar los archivos con `git add .`.    
4. Hacer un commit con `git commit -m "Nuevos módulos"`.
5. Subir cambios: git push -u origin rama-1.

Método 2: Cuando ya tienes un repositorio local y quieres subirlo a un repositorio existente en GitHub.
1. Inicializar un reposotorio local con `git init`.
2. Agregar los archivos con `git add .`.
3. Hacer un commit con `git commit -m "Nuevos módulos"`.
4. Agregar el repositorio remoto con `git remote add origin https:....`.
5. Unicar cambios  git pull origin master --allow-unrelated-histories
6. Subir cambios: git push -u origin master.


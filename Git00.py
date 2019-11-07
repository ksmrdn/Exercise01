print('Rachmad pasti bisa!')

#staging area --> add
#commit --> commit
#git add . -> semua
#git add nama_file.py
#git status --> cek status --> cek dulu sebelum melakukan apa-apa
#git rm --cached nama_file --> hapus file
#git commit -m "My first commit"
#git log --> ada berapa commit
#git log --oneline --> singkat
#add --> commit --> log
# A --> Siap di commit
# U --> Belum siap di commit
# M --> Modify
#git checkout IDcommit --> lihat doang back to IDcommit, diharamkan mengubah isi file
#git checkout master --> lihat ke paling up to date, diharamkan mengubah isi file

#========= commit 1 ============== commit 2 =============== commit 3
#^ pake checkout hanya lihat ^

#========= commit 1 
#git reset IDCommit1 --> come back to id commit dan 
# commit setelahya hilang
#git reset IDCommit1 --hard --> balik ke awal, file yang dihapus kembali lagi

#========= commit 1 ============== commit 2 =============== commit 3
#                                        ||            ||
#                                        ||            ||
#                                         commit branch 1
#git branch namabranch
#git branch -a --> melihat branch apa aja & posisi kita
#git checkout master --> melihat apa kita sudah di master
#git branch -D namabranch --> delete branch
#git merge namabranch --> masukkan branch ke master
#git checkout -b namabranch --> masukkan nama branch sekaligus ke branch tersebut
#git remote add rain01 https://github.com/ksmrdn/Exercise01.git
#git push rain01 master --> create repository
#git clone linkclonegithub

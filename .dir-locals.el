(
 (nil .
      ((projectile-project-run-cmd . "./yan_list_all.py")
       (eval . (progn
                 (defun auto_pass (args)
                   "docstring"
                   (shell-command-to-string "pass kubuntu-pass"))
                 (defun set_com_hook ()
                   "docstring"
                   (setq comint-password-function #'auto_pass)
                   (message "set_com_hook"))
                 (add-hook 'comint-mode-hook 'set_com_hook))))))

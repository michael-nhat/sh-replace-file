(projectile-run-project t)

(defun auto_pass (args)
  "docstring"
  "n;88"
  )

;; run
(setq password-cache)
(setq password-cache-expiry 3600)
(setq comint-password-function #'auto_pass)
(setq comint-password-prompt-regexp )



(defun set_com_hook ()
  "docstring"
  (setq comint-password-function #'auto_pass)
  (message "set_com_hook")
  )

(add-hook 'comint-mode-hook 'set_com_hook)
(remove-hook 'comint-mode-hook 'set_com_hook)

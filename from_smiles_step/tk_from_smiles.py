# -*- coding: utf-8 -*-
"""The graphical part of a fromSMILES node"""

import molssi_workflow
import from_smiles_step
import tkinter as tk
import tkinter.ttk as ttk


class TkFromSMILES(molssi_workflow.TkNode):
    """node_class is the class of the 'real' node that this
    class is the Tk graphics partner for
    """

    node_class = from_smiles_step.FromSMILESNode

    def __init__(self, node=None, canvas=None, x=None, y=None, w=None, h=None):
        '''Initialize a node

        Keyword arguments:
        '''
        super().__init__(node=node, canvas=canvas, x=x, y=y, w=w, h=h)

    def right_click(self, event):
        """Probably need to add our dialog...
        """

        super().right_click(event)
        self.popup_menu.add_command(label="Edit..", command=self.edit)

        self.popup_menu.tk_popup(event.x_root, event.y_root, 0)

    def edit(self):
        """Present a dialog for editing the SMILES string
        """

        dialog = tk.Toplevel()
        self._tmp = {'dialog': dialog}
        dialog.title('From SMILES...')

        frame = ttk.Frame(dialog)
        frame.pack(side='top', fill=tk.BOTH, expand=1)
        smiles_label = ttk.Label(frame, text='SMILES string:')
        smiles = ttk.Entry(frame)
        self._tmp['smiles'] = smiles
        smiles.insert(0, self.node.smiles_string)
        smiles_label.grid(row=0, column=0)
        smiles.grid(row=0, column=1, sticky=tk.E+tk.W)

        button_box = ttk.Frame(dialog)
        button_box.pack(side='bottom', fill=tk.BOTH)

        ok_button = ttk.Button(button_box, text="OK", command=self.handle_ok)
        ok_button.pack(side='left')
        help_button = ttk.Button(
            button_box, text="Help", command=self.handle_help)
        help_button.pack(side='left')
        cancel_button = ttk.Button(
            button_box, text="Cancel", command=self.handle_cancel)
        cancel_button.pack(side='left')

    def handle_ok(self):
        self.node.smiles_string = self._tmp['smiles'].get()
        self._tmp['dialog'].destroy()
        self._tmp = None

    def handle_help(self):
        print('Help')
        self._tmp['dialog'].destroy()
        self._tmp = None

    def handle_cancel(self):
        self._tmp['dialog'].destroy()
        self._tmp = None
#!/usr/bin/python

## @svm_json.py
#  This file contains methods to convert svm data to a JSON object.
import json, csv
from collections import defaultdict
from itertools import islice

## Class: JSON
class JSON:

  ## constructor
  def __init__(self, svm_file):
    self.svm_file = svm_file

  ## csv_to_json: convert csv file to JSON object
  #
  #  Note: we use the 'Universal Newline Support' with the 'U" parameter
  #        when opening 'self.svm_file'. This allows newlines to be
  #        understood regardless, if the newline character was created in
  #        osx, windows, or linux.
  #
  #  Note: since 'row' is a list, with one comma-delimited string element,
  #        the following line is required in this method:
  #
  #            row = row[0].split(',')
  #
  def csv_to_json(self):
    list_dataset         = []
    dep_variable_label   = []
    indep_variable_label = []

    # open temporary 'csvfile' reader object
    with open( self.svm_file, 'rU' ) as csvfile:
      dataset_reader = csv.reader( csvfile, delimiter=' ', quotechar='|' )

      # iterate first row of csvfile
      for row in islice( dataset_reader, 0, 1 ):

        # iterate each column in a given row
        row_indep_label = row[0].split(',')
        for value in islice( row_indep_label, 1, None ):
          indep_variable_label.append( value )

      # iterate all rows of csvfile
      for dep_index, row in enumerate( islice( dataset_reader, 0, None ) ):

        # iterate first column of each row (except first)
        row_dep_label = row[0].split(',')
        for value in row_dep_label[:1]:
          dep_variable_label.append( value )

        # iterate each column in a given row
        row_indep_variable = row[0].split(',')
        for indep_index, value in enumerate( islice( row_indep_variable, 1, None) ):
          try:

          except Exception as e:
            print e
            return False

          list_dataset.append( { 'dep_variable_label': dep_variable_label[dep_index], 'indep_variable_label': indep_variable_label[indep_index], 'indep_variable_value': value} )

    return json.dumps( list_dataset )

  ## xml_to_json: convert xml to JSON object
  def xml_to_json(self):
    print 'dummy code'

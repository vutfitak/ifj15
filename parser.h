/*
 * Course IFJ @ FIT VUT Brno, 2015
 * IFJ15 Interpreter Project
 *
 * Authors:
 * Lukas Osadsky  - xosads00
 * Pavol Plaskon  - xplask00
 * Pavel Pospisil - xpospi88
 * Matej Postolka - xposto02
 *
 * Unless otherwise stated, all code is licensed under a
 * GNU General Public License v2.0
 *
 */

 /**
  * @file parser.h
  * @brief Syntax analysis - parser
  *
  * This is the main parser of tokens.
  *
  */

  #ifndef PARSER_H
  #define PARSER_H

  /**
  * @brief Parse the source file
  *
  * Start the syntax analyzer and begin parsing the source
  *
  * @param *fp Pointer to file with IFJ15 source code
  */
  void parse();

  #endif // PARSER_H

/*
 * =====================================================================================
 *
 *       Filename:  CSCDQM_Collection.h
 *
 *    Description:  Histogram Collection management class
 *
 *        Version:  1.0
 *        Created:  10/30/2008 04:40:38 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Valdas Rapsevicius (VR), valdas.rapsevicius@cern.ch
 *        Company:  CERN, CH
 *
 * =====================================================================================
 */

#ifndef CSCDQM_Collection_H
#define CSCDQM_Collection_H

#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <TProfile.h>

#include <xercesc/parsers/XercesDOMParser.hpp>
#include <xercesc/dom/DOMNodeList.hpp>
#include <xercesc/dom/DOMElement.hpp>

#include <boost/shared_ptr.hpp>

#include "DQM/CSCMonitorModule/interface/CSCDQM_Exception.h"
#include "DQM/CSCMonitorModule/interface/CSCDQM_Logger.h"
#include "DQM/CSCMonitorModule/interface/CSCDQM_Utility.h"
#include "DQM/CSCMonitorModule/interface/CSCDQM_Configuration.h"

namespace cscdqm {

  using namespace XERCES_CPP_NAMESPACE;

  static const char XML_BOOK_DEFINITION[]     =  "Definition";
  static const char XML_BOOK_DEFINITION_ID[]  =  "id";
  static const char XML_BOOK_HISTOGRAM[]      =  "Histogram";
  static const char XML_BOOK_DEFINITION_REF[] =  "ref";
  static const char XML_BOOK_HISTO_NAME[]     =  "Name";
  static const char XML_BOOK_HISTO_PREFIX[]   =  "Prefix";
  static const char XML_BOOK_HISTO_TYPE[]     =  "Type";
  static const char XML_BOOK_HISTO_TITLE[]    =  "Title";
  static const char XML_BOOK_ONDEMAND[]       =  "OnDemand";
  static const char XML_BOOK_ONDEMAND_TRUE[]  =  "1";
  static const char XML_BOOK_ONDEMAND_FALSE[] =  "0";

  static const int  DEF_HISTO_COLOR           =  48;

  /**
  * Type Definition Section
  */
  typedef std::map<std::string, std::string>     CoHistoProps;
  typedef std::map<std::string, CoHistoProps>    CoHisto;
  typedef std::map<std::string, CoHisto>         CoHistoMap;
  
  /**
   * @class Collection
   * @brief Manage collection of histograms, load histogram definitions from
   * XML file and book histograms by calling MonitorObjectProvider routines.  
   */
  class Collection {

    public:

      Collection(Configuration* const p_config);

      void bookEMUHistos() const;
      void bookDDUHistos(const HwId dduId) const;
      void bookCSCHistos(const HwId crateId, const HwId dmbId) const;
      void bookCSCHistos(const HistoId hid, const HwId crateId, const HwId dmbId, const HwId addId) const;

      const bool isOnDemand(const HistoName& name) const;

      void printCollection() const;

    private:
      
      static const bool checkHistoValue(const CoHistoProps& h, const std::string& name, std::string& value);
      static const bool checkHistoValue(const CoHistoProps& h, const std::string& name, int& value);
      static const bool checkHistoValue(const CoHistoProps& h, const std::string name, double& value);

      static std::string& getHistoValue(const CoHistoProps& h, const std::string& name, std::string& value, const std::string& def_value = "");
      static int&         getHistoValue(const CoHistoProps& h, const std::string& name, int& value, const int& def_value = 0);
      static double&      getHistoValue(const CoHistoProps& h, const std::string name, double& value, const int def_value = 0.0);
      
      void load();
      void book(const HistoDef& h, const CoHistoProps& h, const std::string& folder) const;
      static const int ParseAxisLabels(const std::string& s, std::map<int, std::string>& labels);
      static void getNodeProperties(DOMNode*& node, CoHistoProps& hp);
      
      Configuration*         config;

      CoHistoMap             collection;

  };

}

#endif

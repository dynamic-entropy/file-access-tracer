# CMS RSE access-capture status

Auto-generated from [`sites.csv`](sites.csv). **CSV is the source of truth** for scripts; this Markdown is for browsing on GitHub.

Regenerate: `python scripts/render_sites_md.py`

## Summary

| tracer_status | count |
|---------------|------:|
| ⚪ `not_started` | 261 |

| storage_tech | count |
|--------------|------:|
| `XRootD` | 133 |
| `dCache` | 53 |
| `EOS` | 39 |
| `unknown` | 32 |
| `StoRM` | 4 |

| last_probe_result | count |
|-------------------|------:|
| — | 261 |

## Legend

| Status | Meaning |
|--------|---------|
| ⚪ `not_started` | In inventory; no instrumentation yet |
| 🟡 `instrumented` | Capture configured at site |
| ✅ `validated` | place→read→capture probe passed |
| 🚫 `blocked` | Cannot instrument yet |
| ⬛ `out_of_scope` | Explicitly skipped |

## All RSEs

| status | rse | site | tier | tech | method | protocol | endpoint | probe |
|--------|-----|------|------|------|--------|----------|----------|-------|
| ⚪ `not_started` | `T0_CH_CERN_Disk` | T0_CH_CERN | 0 | `EOS` | `ofs.notify` | `root` | `root://eoscms.cern.ch:1094/` | — |
| ⚪ `not_started` | `T0_CH_CERN_Disk_Test` | T0_CH_CERN | 0 | `EOS` | `ofs.notify` | `root` | `root://eoscms.cern.ch:1094/` | — |
| ⚪ `not_started` | `T0_CH_CERN_Tape` | T0_CH_CERN | 0 | `EOS` | `ofs.notify` | `davs` | `davs://eosctacms.cern.ch:8444//eos/ctacms/archive/cms/` | — |
| ⚪ `not_started` | `T0_CH_CERN_Tape_Test` | T0_CH_CERN | 0 | `EOS` | `ofs.notify` | `davs` | `davs://eosctacms.cern.ch:8444//eos/ctacms/archive/cms/store/test/rucio/` | — |
| ⚪ `not_started` | `T1_DE_KIT_Disk` | T1_DE_KIT | 1 | `dCache` | `dcache.kafka` | `root` | `root://cmsdcache-kit-disk.gridka.de:1094/` | — |
| ⚪ `not_started` | `T1_DE_KIT_Disk_Temp` | T1_DE_KIT | 1 | `dCache` | `dcache.kafka` | `root` | `root://cmsdcache-kit-disk.gridka.de:1094/` | — |
| ⚪ `not_started` | `T1_DE_KIT_Disk_Test` | T1_DE_KIT | 1 | `dCache` | `dcache.kafka` | `root` | `root://cmsdcache-kit-disk.gridka.de:1094/` | — |
| ⚪ `not_started` | `T1_DE_KIT_Tape` | T1_DE_KIT | 1 | `dCache` | `dcache.kafka` | `davs` | `davs://cmsdcache-kit-tape.gridka.de:2880/` | — |
| ⚪ `not_started` | `T1_DE_KIT_Tape_Test` | T1_DE_KIT | 1 | `dCache` | `dcache.kafka` | `davs` | `davs://cmsdcache-kit-tape.gridka.de:2880/pnfs/gridka.de/cms/tape/store/test/rucio/` | — |
| ⚪ `not_started` | `T1_ES_PIC_Disk` | T1_ES_PIC | 1 | `dCache` | `dcache.kafka` | `root` | `root://xrootd-cmst1-door.pic.es:1094/` | — |
| ⚪ `not_started` | `T1_ES_PIC_Disk_Temp` | T1_ES_PIC | 1 | `dCache` | `dcache.kafka` | `root` | `root://xrootd-cmst1-door.pic.es:1094/` | — |
| ⚪ `not_started` | `T1_ES_PIC_Disk_Test` | T1_ES_PIC | 1 | `dCache` | `dcache.kafka` | `root` | `root://xrootd-cmst1-door.pic.es:1094/` | — |
| ⚪ `not_started` | `T1_ES_PIC_Tape` | T1_ES_PIC | 1 | `dCache` | `dcache.kafka` | `davs` | `davs://webdav-cms-tape.pic.es:8450/pnfs/pic.es/data/cms/` | — |
| ⚪ `not_started` | `T1_ES_PIC_Tape_Test` | T1_ES_PIC | 1 | `dCache` | `dcache.kafka` | `davs` | `davs://webdav-cms-tape.pic.es:8450/pnfs/pic.es/data/cms/store/test/rucio/` | — |
| ⚪ `not_started` | `T1_FR_CCIN2P3_Disk` | T1_FR_CCIN2P3 | 1 | `XRootD` | `ofs.notify` | `root` | `root://ccxrdcms.in2p3.fr:1094/` | — |
| ⚪ `not_started` | `T1_FR_CCIN2P3_Disk_Temp` | T1_FR_CCIN2P3 | 1 | `XRootD` | `ofs.notify` | `root` | `root://ccxrdcms.in2p3.fr:1094/` | — |
| ⚪ `not_started` | `T1_FR_CCIN2P3_Disk_Test` | T1_FR_CCIN2P3 | 1 | `XRootD` | `ofs.notify` | `root` | `root://ccxrdcms.in2p3.fr:1094/` | — |
| ⚪ `not_started` | `T1_FR_CCIN2P3_Tape` | T1_FR_CCIN2P3 | 1 | `XRootD` | `ofs.notify` | `root` | `root://ccxrdcms.in2p3.fr:1094/` | — |
| ⚪ `not_started` | `T1_FR_CCIN2P3_Tape_Test` | T1_FR_CCIN2P3 | 1 | `dCache` | `dcache.kafka` | `root` | `root://ccxrdcms.in2p3.fr:1094/` | — |
| ⚪ `not_started` | `T1_IT_CNAF_Disk` | T1_IT_CNAF | 1 | `XRootD` | `ofs.notify` | `root` | `root://xrootd-cms.infn.it:1194/` | — |
| ⚪ `not_started` | `T1_IT_CNAF_Disk_Temp` | T1_IT_CNAF | 1 | `XRootD` | `ofs.notify` | `root` | `root://xrootd-cms.infn.it:1194/` | — |
| ⚪ `not_started` | `T1_IT_CNAF_Disk_Test` | T1_IT_CNAF | 1 | `XRootD` | `ofs.notify` | `root` | `root://xrootd-cms.infn.it:1194/` | — |
| ⚪ `not_started` | `T1_IT_CNAF_Tape` | T1_IT_CNAF | 1 | `unknown` | `unknown` | `davs` | `davs://xfer-tape-cms.cr.cnaf.infn.it:8443/cmstape/` | — |
| ⚪ `not_started` | `T1_IT_CNAF_Tape_Test` | T1_IT_CNAF | 1 | `unknown` | `unknown` | `davs` | `davs://xfer-tape-cms.cr.cnaf.infn.it:8443/cmstape/store/test/rucio/` | — |
| ⚪ `not_started` | `T1_PL_NCBJ_Disk` | T1_PL_NCBJ | 1 | `XRootD` | `ofs.notify` | `root` | `root://se.cis.gov.pl:1094/` | — |
| ⚪ `not_started` | `T1_PL_NCBJ_Disk_Temp` | T1_PL_NCBJ | 1 | `XRootD` | `ofs.notify` | `root` | `root://se.cis.gov.pl:1094/` | — |
| ⚪ `not_started` | `T1_PL_NCBJ_Disk_Test` | T1_PL_NCBJ | 1 | `XRootD` | `ofs.notify` | `root` | `root://se.cis.gov.pl:1094/` | — |
| ⚪ `not_started` | `T1_PL_NCBJ_Tape` | T1_PL_NCBJ | 1 | `XRootD` | `ofs.notify` | `root` | `root://tape-cms.cis.gov.pl:1094/` | — |
| ⚪ `not_started` | `T1_RU_JINR_Disk` | T1_RU_JINR | 1 | `dCache` | `dcache.kafka` | `root` | `root://xrootd01.jinr-t1.ru:1094/` | — |
| ⚪ `not_started` | `T1_RU_JINR_Disk_Temp` | T1_RU_JINR | 1 | `dCache` | `dcache.kafka` | `root` | `root://xrootd01.jinr-t1.ru:1094/` | — |
| ⚪ `not_started` | `T1_RU_JINR_Disk_Test` | T1_RU_JINR | 1 | `dCache` | `dcache.kafka` | `root` | `root://xrootd01.jinr-t1.ru:1094/` | — |
| ⚪ `not_started` | `T1_RU_JINR_Tape` | T1_RU_JINR | 1 | `dCache` | `dcache.kafka` | `davs` | `davs://se-wbdv-mss.jinr-t1.ru:2880/pnfs/jinr-t1.ru/data/cms/` | — |
| ⚪ `not_started` | `T1_RU_JINR_Tape_Test` | T1_RU_JINR | 1 | `dCache` | `dcache.kafka` | `davs` | `davs://se-wbdv-mss.jinr-t1.ru:2880/pnfs/jinr-t1.ru/data/cms/store/test/rucio/` | — |
| ⚪ `not_started` | `T1_UK_RAL_Disk` | T1_UK_RAL | 1 | `XRootD` | `ofs.notify` | `root` | `root://rdr.echo.stfc.ac.uk:1094/` | — |
| ⚪ `not_started` | `T1_UK_RAL_Disk_Temp` | T1_UK_RAL | 1 | `XRootD` | `ofs.notify` | `root` | `root://rdr.echo.stfc.ac.uk:1094/` | — |
| ⚪ `not_started` | `T1_UK_RAL_Disk_Test` | T1_UK_RAL | 1 | `XRootD` | `ofs.notify` | `root` | `root://rdr.echo.stfc.ac.uk:1094/` | — |
| ⚪ `not_started` | `T1_UK_RAL_Tape` | T1_UK_RAL | 1 | `EOS` | `ofs.notify` | `root` | `root://antares.stfc.ac.uk:1094/` | — |
| ⚪ `not_started` | `T1_UK_RAL_Tape_Test` | T1_UK_RAL | 1 | `EOS` | `ofs.notify` | `root` | `root://antares.stfc.ac.uk:1094/` | — |
| ⚪ `not_started` | `T1_US_FNAL_Disk` | T1_US_FNAL | 1 | `dCache` | `dcache.kafka` | `root` | `root://cmsdcadisk.fnal.gov:1094/` | — |
| ⚪ `not_started` | `T1_US_FNAL_Disk_Temp` | T1_US_FNAL | 1 | `dCache` | `dcache.kafka` | `root` | `root://cmsdcadisk.fnal.gov:1094/` | — |
| ⚪ `not_started` | `T1_US_FNAL_Disk_Test` | T1_US_FNAL | 1 | `dCache` | `dcache.kafka` | `root` | `root://cmsdcadisk.fnal.gov:1094/` | — |
| ⚪ `not_started` | `T1_US_FNAL_Tape` | T1_US_FNAL | 1 | `unknown` | `unknown` | `davs` | `davs://cmsdcatape.fnal.gov:2880/WAX/11/` | — |
| ⚪ `not_started` | `T1_US_FNAL_Tape_Test` | T1_US_FNAL | 1 | `unknown` | `unknown` | `davs` | `davs://cmstnvm1.fnal.gov:2880/` | — |
| ⚪ `not_started` | `T2_AT_Vienna` | T2_AT_Vienna | 2 | `EOS` | `ofs.notify` | `root` | `root://eos.grid.vbc.ac.at:1094/` | — |
| ⚪ `not_started` | `T2_AT_Vienna_Temp` | T2_AT_Vienna | 2 | `EOS` | `ofs.notify` | `root` | `root://eos.grid.vbc.ac.at:1094/` | — |
| ⚪ `not_started` | `T2_AT_Vienna_Test` | T2_AT_Vienna | 2 | `EOS` | `ofs.notify` | `root` | `root://eos.grid.vbc.ac.at:1094/` | — |
| ⚪ `not_started` | `T2_BE_IIHE` | T2_BE_IIHE | 2 | `dCache` | `dcache.kafka` | `root` | `root://maite.iihe.ac.be:1094/` | — |
| ⚪ `not_started` | `T2_BE_IIHE_Temp` | T2_BE_IIHE | 2 | `dCache` | `dcache.kafka` | `root` | `root://maite.iihe.ac.be:1094/` | — |
| ⚪ `not_started` | `T2_BE_IIHE_Test` | T2_BE_IIHE | 2 | `dCache` | `dcache.kafka` | `root` | `root://maite.iihe.ac.be:1094/` | — |
| ⚪ `not_started` | `T2_BE_UCL` | T2_BE_UCL | 2 | `unknown` | `unknown` | `davs` | `davs://ingrid-se02.cism.ucl.ac.be:1094/` | — |
| ⚪ `not_started` | `T2_BE_UCL_Temp` | T2_BE_UCL | 2 | `unknown` | `unknown` | `davs` | `davs://ingrid-se02.cism.ucl.ac.be:1094/store/temp/` | — |
| ⚪ `not_started` | `T2_BE_UCL_Test` | T2_BE_UCL | 2 | `unknown` | `unknown` | `davs` | `davs://ingrid-se02.cism.ucl.ac.be:1094/store/test/rucio/` | — |
| ⚪ `not_started` | `T2_BR_SPRACE` | T2_BR_SPRACE | 2 | `XRootD` | `ofs.notify` | `root` | `root://osg-se.sprace.org.br:1094/` | — |
| ⚪ `not_started` | `T2_BR_SPRACE_Temp` | T2_BR_SPRACE | 2 | `XRootD` | `ofs.notify` | `root` | `root://osg-se.sprace.org.br:1094/` | — |
| ⚪ `not_started` | `T2_BR_SPRACE_Test` | T2_BR_SPRACE | 2 | `XRootD` | `ofs.notify` | `root` | `root://osg-se.sprace.org.br:1094/` | — |
| ⚪ `not_started` | `T2_BR_UERJ` | T2_BR_UERJ | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootd2.hepgrid.uerj.br:1094/` | — |
| ⚪ `not_started` | `T2_BR_UERJ_Temp` | T2_BR_UERJ | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootd2.hepgrid.uerj.br:1094/` | — |
| ⚪ `not_started` | `T2_BR_UERJ_Test` | T2_BR_UERJ | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootd2.hepgrid.uerj.br:1094/` | — |
| ⚪ `not_started` | `T2_CH_CERN` | T2_CH_CERN | 2 | `EOS` | `ofs.notify` | `root` | `root://eoscms.cern.ch:1094/` | — |
| ⚪ `not_started` | `T2_CH_CERN_Temp` | T2_CH_CERN | 2 | `EOS` | `ofs.notify` | `root` | `root://eoscms.cern.ch:1094/` | — |
| ⚪ `not_started` | `T2_CH_CERN_Test` | T2_CH_CERN | 2 | `EOS` | `ofs.notify` | `root` | `root://eoscms.cern.ch:1094/` | — |
| ⚪ `not_started` | `T2_CH_CSCS` | T2_CH_CSCS | 2 | `dCache` | `dcache.kafka` | `root` | `root://storage01.lcg.cscs.ch:1096/` | — |
| ⚪ `not_started` | `T2_CH_CSCS_Temp` | T2_CH_CSCS | 2 | `dCache` | `dcache.kafka` | `root` | `root://storage01.lcg.cscs.ch:1096/` | — |
| ⚪ `not_started` | `T2_CH_CSCS_Test` | T2_CH_CSCS | 2 | `dCache` | `dcache.kafka` | `root` | `root://storage01.lcg.cscs.ch:1096/` | — |
| ⚪ `not_started` | `T2_CN_Beijing` | T2_CN_Beijing | 2 | `EOS` | `ofs.notify` | `root` | `root://cceos.ihep.ac.cn:1094/` | — |
| ⚪ `not_started` | `T2_CN_Beijing_Temp` | T2_CN_Beijing | 2 | `EOS` | `ofs.notify` | `root` | `root://cceos.ihep.ac.cn:1094/` | — |
| ⚪ `not_started` | `T2_CN_Beijing_Test` | T2_CN_Beijing | 2 | `EOS` | `ofs.notify` | `root` | `root://cceos.ihep.ac.cn:1094/` | — |
| ⚪ `not_started` | `T2_DE_DESY` | T2_DE_DESY | 2 | `dCache` | `dcache.kafka` | `root` | `root://dcache-cms-xrootd.desy.de:1094/` | — |
| ⚪ `not_started` | `T2_DE_DESY_Tape` | T2_DE_DESY | 2 | `dCache` | `dcache.kafka` | `davs` | `davs://dcache-cms-tape.desy.de:2880/` | — |
| ⚪ `not_started` | `T2_DE_DESY_Temp` | T2_DE_DESY | 2 | `dCache` | `dcache.kafka` | `root` | `root://dcache-cms-xrootd.desy.de:1094/` | — |
| ⚪ `not_started` | `T2_DE_DESY_Test` | T2_DE_DESY | 2 | `dCache` | `dcache.kafka` | `root` | `root://dcache-cms-xrootd.desy.de:1094/` | — |
| ⚪ `not_started` | `T2_DE_RWTH` | T2_DE_RWTH | 2 | `XRootD` | `ofs.notify` | `root` | `root://grid-cms-xrootd.physik.rwth-aachen.de:1094/` | — |
| ⚪ `not_started` | `T2_DE_RWTH_Temp` | T2_DE_RWTH | 2 | `XRootD` | `ofs.notify` | `root` | `root://grid-cms-xrootd.physik.rwth-aachen.de:1094/` | — |
| ⚪ `not_started` | `T2_DE_RWTH_Test` | T2_DE_RWTH | 2 | `XRootD` | `ofs.notify` | `root` | `root://grid-cms-xrootd.physik.rwth-aachen.de:1094/` | — |
| ⚪ `not_started` | `T2_EE_Estonia` | T2_EE_Estonia | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootd.hep.kbfi.ee:1094/` | — |
| ⚪ `not_started` | `T2_EE_Estonia_Temp` | T2_EE_Estonia | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootd.hep.kbfi.ee:1094/` | — |
| ⚪ `not_started` | `T2_EE_Estonia_Test` | T2_EE_Estonia | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootd.hep.kbfi.ee:1094/` | — |
| ⚪ `not_started` | `T2_ES_CIEMAT` | T2_ES_CIEMAT | 2 | `dCache` | `dcache.kafka` | `root` | `root://gaexrdoor.ciemat.es:1094/` | — |
| ⚪ `not_started` | `T2_ES_CIEMAT_Temp` | T2_ES_CIEMAT | 2 | `dCache` | `dcache.kafka` | `root` | `root://gaexrdoor.ciemat.es:1094/` | — |
| ⚪ `not_started` | `T2_ES_CIEMAT_Test` | T2_ES_CIEMAT | 2 | `dCache` | `dcache.kafka` | `root` | `root://gaexrdoor.ciemat.es:1094/` | — |
| ⚪ `not_started` | `T2_ES_IFCA` | T2_ES_IFCA | 2 | `XRootD` | `ofs.notify` | `root` | `root://gridftp.ifca.es:1094/` | — |
| ⚪ `not_started` | `T2_ES_IFCA_Temp` | T2_ES_IFCA | 2 | `XRootD` | `ofs.notify` | `root` | `root://gridftp.ifca.es:1094/` | — |
| ⚪ `not_started` | `T2_ES_IFCA_Test` | T2_ES_IFCA | 2 | `XRootD` | `ofs.notify` | `root` | `root://gridftp.ifca.es:1094/` | — |
| ⚪ `not_started` | `T2_FI_HIP` | T2_FI_HIP | 2 | `XRootD` | `ofs.notify` | `root` | `root://hip-cms-se.csc.fi:1094/` | — |
| ⚪ `not_started` | `T2_FI_HIP_Temp` | T2_FI_HIP | 2 | `XRootD` | `ofs.notify` | `root` | `root://hip-cms-se.csc.fi:1094/` | — |
| ⚪ `not_started` | `T2_FI_HIP_Test` | T2_FI_HIP | 2 | `XRootD` | `ofs.notify` | `root` | `root://hip-cms-se.csc.fi:1094/` | — |
| ⚪ `not_started` | `T2_FR_GRIF` | T2_FR_GRIF | 2 | `EOS` | `ofs.notify` | `davs` | `davs://eos.grif.fr:11000/eos/grif/cms/grif/` | — |
| ⚪ `not_started` | `T2_FR_GRIF_IRFU` | T2_FR_GRIF_IRFU | 2 | `EOS` | `ofs.notify` | `davs` | `davs://eos.grif.fr:11000/eos/grif/cms/irfu/` | — |
| ⚪ `not_started` | `T2_FR_GRIF_IRFU_Temp` | T2_FR_GRIF_IRFU | 2 | `EOS` | `ofs.notify` | `davs` | `davs://eos.grif.fr:11000/eos/grif/cms/irfu/store/temp/` | — |
| ⚪ `not_started` | `T2_FR_GRIF_IRFU_Test` | T2_FR_GRIF_IRFU | 2 | `EOS` | `ofs.notify` | `davs` | `davs://eos.grif.fr:11000/eos/grif/cms/irfu/store/test/rucio/` | — |
| ⚪ `not_started` | `T2_FR_GRIF_LLR` | T2_FR_GRIF_LLR | 2 | `EOS` | `ofs.notify` | `davs` | `davs://eos.grif.fr:11000/eos/grif/cms/llr/` | — |
| ⚪ `not_started` | `T2_FR_GRIF_LLR_Temp` | T2_FR_GRIF_LLR | 2 | `EOS` | `ofs.notify` | `davs` | `davs://eos.grif.fr:11000/eos/grif/cms/llr/store/temp/` | — |
| ⚪ `not_started` | `T2_FR_GRIF_LLR_Test` | T2_FR_GRIF_LLR | 2 | `EOS` | `ofs.notify` | `davs` | `davs://eos.grif.fr:11000/eos/grif/cms/llr/store/test/rucio/` | — |
| ⚪ `not_started` | `T2_FR_GRIF_Temp` | T2_FR_GRIF | 2 | `EOS` | `ofs.notify` | `davs` | `davs://eos.grif.fr:11000/eos/grif/cms/grif/store/temp/` | — |
| ⚪ `not_started` | `T2_FR_IPHC` | T2_FR_IPHC | 2 | `dCache` | `dcache.kafka` | `root` | `root://sbgdcache.in2p3.fr:1094/` | — |
| ⚪ `not_started` | `T2_FR_IPHC_Temp` | T2_FR_IPHC | 2 | `dCache` | `dcache.kafka` | `root` | `root://sbgdcache.in2p3.fr:1094/` | — |
| ⚪ `not_started` | `T2_FR_IPHC_Test` | T2_FR_IPHC | 2 | `dCache` | `dcache.kafka` | `root` | `root://sbgdcache.in2p3.fr:1094/` | — |
| ⚪ `not_started` | `T2_GR_Ioannina_Temp` | T2_GR_Ioannina | 2 | `unknown` | `unknown` | `srm` | `srm://grid02.physics.uoi.gr:8446/dpm/physics.uoi.gr/home/cms/store/temp/` | — |
| ⚪ `not_started` | `T2_GR_Ioannina_Test` | T2_GR_Ioannina | 2 | `unknown` | `unknown` | `srm` | `srm://grid02.physics.uoi.gr:8446/dpm/physics.uoi.gr/home/cms/store/test/rucio/` | — |
| ⚪ `not_started` | `T2_HU_Budapest` | T2_HU_Budapest | 2 | `XRootD` | `ofs.notify` | `root` | `root://grid143.kfki.hu:1094/` | — |
| ⚪ `not_started` | `T2_HU_Budapest_Temp` | T2_HU_Budapest | 2 | `XRootD` | `ofs.notify` | `root` | `root://grid143.kfki.hu:1094/` | — |
| ⚪ `not_started` | `T2_HU_Budapest_Test` | T2_HU_Budapest | 2 | `XRootD` | `ofs.notify` | `root` | `root://grid143.kfki.hu:1094/` | — |
| ⚪ `not_started` | `T2_IN_TIFR` | T2_IN_TIFR | 2 | `XRootD` | `ofs.notify` | `root` | `root://t2se.indiacms.res.in:1094/` | — |
| ⚪ `not_started` | `T2_IN_TIFR_Temp` | T2_IN_TIFR | 2 | `XRootD` | `ofs.notify` | `root` | `root://t2se.indiacms.res.in:1094/` | — |
| ⚪ `not_started` | `T2_IN_TIFR_Test` | T2_IN_TIFR | 2 | `XRootD` | `ofs.notify` | `root` | `root://t2se.indiacms.res.in:1094/` | — |
| ⚪ `not_started` | `T2_IT_Bari` | T2_IT_Bari | 2 | `unknown` | `unknown` | `davs` | `davs://webdav.recas.ba.infn.it:8443/cms/` | — |
| ⚪ `not_started` | `T2_IT_Bari_Temp` | T2_IT_Bari | 2 | `unknown` | `unknown` | `davs` | `davs://webdav.recas.ba.infn.it:8443/cms/store/temp/` | — |
| ⚪ `not_started` | `T2_IT_Bari_Test` | T2_IT_Bari | 2 | `unknown` | `unknown` | `davs` | `davs://webdav.recas.ba.infn.it:8443/cms/store/test/rucio/` | — |
| ⚪ `not_started` | `T2_IT_Legnaro` | T2_IT_Legnaro | 2 | `dCache` | `dcache.kafka` | `root` | `root://t2-xrdcms.lnl.infn.it:7070/` | — |
| ⚪ `not_started` | `T2_IT_Legnaro_Temp` | T2_IT_Legnaro | 2 | `dCache` | `dcache.kafka` | `root` | `root://t2-xrdcms.lnl.infn.it:7070/` | — |
| ⚪ `not_started` | `T2_IT_Legnaro_Test` | T2_IT_Legnaro | 2 | `dCache` | `dcache.kafka` | `root` | `root://t2-xrdcms.lnl.infn.it:7070/` | — |
| ⚪ `not_started` | `T2_IT_Pisa` | T2_IT_Pisa | 2 | `StoRM` | `deferred` | `davs` | `davs://stwebdav.pi.infn.it:8443/cms/` | — |
| ⚪ `not_started` | `T2_IT_Pisa_Temp` | T2_IT_Pisa | 2 | `unknown` | `unknown` | `davs` | `davs://stwebdav.pi.infn.it:8443/cms/store/temp/` | — |
| ⚪ `not_started` | `T2_IT_Pisa_Test` | T2_IT_Pisa | 2 | `unknown` | `unknown` | `davs` | `davs://stwebdav.pi.infn.it:8443/cms/store/test/rucio/` | — |
| ⚪ `not_started` | `T2_IT_Rome` | T2_IT_Rome | 2 | `XRootD` | `ofs.notify` | `davs` | `davs://cmsrm-webdav.roma1.infn.it:2880/` | — |
| ⚪ `not_started` | `T2_IT_Rome_Temp` | T2_IT_Rome | 2 | `unknown` | `unknown` | `davs` | `davs://cmsrm-webdav.roma1.infn.it:2880//temp/` | — |
| ⚪ `not_started` | `T2_IT_Rome_Test` | T2_IT_Rome | 2 | `unknown` | `unknown` | `davs` | `davs://cmsrm-webdav.roma1.infn.it:2880//test/rucio/` | — |
| ⚪ `not_started` | `T2_KR_KISTI` | T2_KR_KISTI | 2 | `XRootD` | `ofs.notify` | `root` | `root://cms-t2-se01.sdfarm.kr:1094/` | — |
| ⚪ `not_started` | `T2_KR_KISTI_Temp` | T2_KR_KISTI | 2 | `XRootD` | `ofs.notify` | `root` | `root://cms-t2-se01.sdfarm.kr:1094/` | — |
| ⚪ `not_started` | `T2_KR_KISTI_Test` | T2_KR_KISTI | 2 | `XRootD` | `ofs.notify` | `root` | `root://cms-t2-se01.sdfarm.kr:1094/` | — |
| ⚪ `not_started` | `T2_LB_HPC4L` | T2_LB_HPC4L | 2 | `EOS` | `ofs.notify` | `root` | `root://mgm.hpc4l.org:1094/` | — |
| ⚪ `not_started` | `T2_LV_HPCNET` | T2_LV_HPCNET | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootd.tier2.hpc-net.lv:1094/` | — |
| ⚪ `not_started` | `T2_PK_NCP` | T2_PK_NCP | 2 | `XRootD` | `ofs.notify` | `root` | `root://pcncp22.ncp.edu.pk:1094/` | — |
| ⚪ `not_started` | `T2_PK_NCP_Temp` | T2_PK_NCP | 2 | `XRootD` | `ofs.notify` | `root` | `root://pcncp22.ncp.edu.pk:1094/` | — |
| ⚪ `not_started` | `T2_PK_NCP_Test` | T2_PK_NCP | 2 | `XRootD` | `ofs.notify` | `root` | `root://pcncp22.ncp.edu.pk:1094/` | — |
| ⚪ `not_started` | `T2_PL_Cyfronet` | T2_PL_Cyfronet | 2 | `EOS` | `ofs.notify` | `root` | `root://eos01.grid.cyfronet.pl:1094/` | — |
| ⚪ `not_started` | `T2_PL_Warsaw` | T2_PL_Warsaw | 2 | `unknown` | `unknown` | `` | `` | — |
| ⚪ `not_started` | `T2_PT_NCG_Lisbon` | T2_PT_NCG_Lisbon | 2 | `XRootD` | `ofs.notify` | `root` | `root://xroot01.ncg.ingrid.pt:1094/` | — |
| ⚪ `not_started` | `T2_PT_NCG_Lisbon_Temp` | T2_PT_NCG_Lisbon | 2 | `XRootD` | `ofs.notify` | `root` | `root://xroot01.ncg.ingrid.pt:1094/` | — |
| ⚪ `not_started` | `T2_PT_NCG_Lisbon_Test` | T2_PT_NCG_Lisbon | 2 | `XRootD` | `ofs.notify` | `root` | `root://xroot01.ncg.ingrid.pt:1094/` | — |
| ⚪ `not_started` | `T2_RC_MOCK` | T2_RC_MOCK | 2 | `unknown` | `unknown` | `` | `` | — |
| ⚪ `not_started` | `T2_RU_IHEP` | T2_RU_IHEP | 2 | `dCache` | `dcache.kafka` | `root` | `root://dp0015.m45.ihep.su:1094/` | — |
| ⚪ `not_started` | `T2_RU_IHEP_Temp` | T2_RU_IHEP | 2 | `dCache` | `dcache.kafka` | `root` | `root://dp0015.m45.ihep.su:1094/` | — |
| ⚪ `not_started` | `T2_RU_IHEP_Test` | T2_RU_IHEP | 2 | `dCache` | `dcache.kafka` | `root` | `root://dp0015.m45.ihep.su:1094/` | — |
| ⚪ `not_started` | `T2_RU_INR` | T2_RU_INR | 2 | `unknown` | `unknown` | `` | `` | — |
| ⚪ `not_started` | `T2_RU_INR_Temp` | T2_RU_INR | 2 | `XRootD` | `ofs.notify` | `root` | `root://grse001.inr.troitsk.ru:1094/` | — |
| ⚪ `not_started` | `T2_RU_INR_Test` | T2_RU_INR | 2 | `XRootD` | `ofs.notify` | `root` | `root://grse001.inr.troitsk.ru:1094/` | — |
| ⚪ `not_started` | `T2_RU_ITEP` | T2_RU_ITEP | 2 | `dCache` | `dcache.kafka` | `root` | `root://se3.itep.ru:1094/` | — |
| ⚪ `not_started` | `T2_RU_ITEP_Temp` | T2_RU_ITEP | 2 | `dCache` | `dcache.kafka` | `root` | `root://se3.itep.ru:1094/` | — |
| ⚪ `not_started` | `T2_RU_ITEP_Test` | T2_RU_ITEP | 2 | `dCache` | `dcache.kafka` | `root` | `root://se3.itep.ru:1094/` | — |
| ⚪ `not_started` | `T2_RU_JINR` | T2_RU_JINR | 2 | `dCache` | `dcache.kafka` | `root` | `root://lcgsedr01.jinr.ru:1094/` | — |
| ⚪ `not_started` | `T2_RU_JINR_Temp` | T2_RU_JINR | 2 | `dCache` | `dcache.kafka` | `root` | `root://lcgsedr01.jinr.ru:1094/` | — |
| ⚪ `not_started` | `T2_RU_JINR_Test` | T2_RU_JINR | 2 | `dCache` | `dcache.kafka` | `root` | `root://lcgsedr01.jinr.ru:1094/` | — |
| ⚪ `not_started` | `T2_TR_METU` | T2_TR_METU | 2 | `XRootD` | `ofs.notify` | `root` | `root://eymir.grid.metu.edu.tr:1094/` | — |
| ⚪ `not_started` | `T2_TR_METU_Temp` | T2_TR_METU | 2 | `XRootD` | `ofs.notify` | `root` | `root://eymir.grid.metu.edu.tr:1094/` | — |
| ⚪ `not_started` | `T2_TR_METU_Test` | T2_TR_METU | 2 | `XRootD` | `ofs.notify` | `root` | `root://eymir.grid.metu.edu.tr:1094/` | — |
| ⚪ `not_started` | `T2_TW_NCHC` | T2_TW_NCHC | 2 | `XRootD` | `ofs.notify` | `root` | `root://se01.grid.nchc.org.tw:1094/` | — |
| ⚪ `not_started` | `T2_TW_NCHC_Temp` | T2_TW_NCHC | 2 | `XRootD` | `ofs.notify` | `root` | `root://se01.grid.nchc.org.tw:1094/` | — |
| ⚪ `not_started` | `T2_TW_NCHC_Test` | T2_TW_NCHC | 2 | `XRootD` | `ofs.notify` | `root` | `root://se01.grid.nchc.org.tw:1094/` | — |
| ⚪ `not_started` | `T2_UA_KIPT` | T2_UA_KIPT | 2 | `XRootD` | `ofs.notify` | `root` | `root://cms-se0.kipt.kharkov.ua:1094/` | — |
| ⚪ `not_started` | `T2_UA_KIPT_Temp` | T2_UA_KIPT | 2 | `XRootD` | `ofs.notify` | `root` | `root://cms-se0.kipt.kharkov.ua:1094/` | — |
| ⚪ `not_started` | `T2_UA_KIPT_Test` | T2_UA_KIPT | 2 | `XRootD` | `ofs.notify` | `root` | `root://cms-se0.kipt.kharkov.ua:1094/` | — |
| ⚪ `not_started` | `T2_UK_London_Brunel` | T2_UK_London_Brunel | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootdgw.brunel.ac.uk:1094/` | — |
| ⚪ `not_started` | `T2_UK_London_Brunel_Temp` | T2_UK_London_Brunel | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootdgw.brunel.ac.uk:1094/` | — |
| ⚪ `not_started` | `T2_UK_London_Brunel_Test` | T2_UK_London_Brunel | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootdgw.brunel.ac.uk:1094/` | — |
| ⚪ `not_started` | `T2_UK_London_IC` | T2_UK_London_IC | 2 | `dCache` | `dcache.kafka` | `root` | `root://gfe02.grid.hep.ph.ic.ac.uk:1094/` | — |
| ⚪ `not_started` | `T2_UK_London_IC_Temp` | T2_UK_London_IC | 2 | `dCache` | `dcache.kafka` | `root` | `root://gfe02.grid.hep.ph.ic.ac.uk:1094/` | — |
| ⚪ `not_started` | `T2_UK_London_IC_Test` | T2_UK_London_IC | 2 | `dCache` | `dcache.kafka` | `root` | `root://gfe02.grid.hep.ph.ic.ac.uk:1094/` | — |
| ⚪ `not_started` | `T2_UK_SGrid_RALPP` | T2_UK_SGrid_RALPP | 2 | `dCache` | `dcache.kafka` | `root` | `root://mover.pp.rl.ac.uk:1094/` | — |
| ⚪ `not_started` | `T2_UK_SGrid_RALPP_Temp` | T2_UK_SGrid_RALPP | 2 | `dCache` | `dcache.kafka` | `root` | `root://mover.pp.rl.ac.uk:1094/` | — |
| ⚪ `not_started` | `T2_UK_SGrid_RALPP_Test` | T2_UK_SGrid_RALPP | 2 | `dCache` | `dcache.kafka` | `root` | `root://mover.pp.rl.ac.uk:1094/` | — |
| ⚪ `not_started` | `T2_US_Caltech` | T2_US_Caltech | 2 | `XRootD` | `ofs.notify` | `root` | `root://k8s-redir.ultralight.org:1094/` | — |
| ⚪ `not_started` | `T2_US_Caltech_Temp` | T2_US_Caltech | 2 | `XRootD` | `ofs.notify` | `root` | `root://k8s-redir.ultralight.org:1094/` | — |
| ⚪ `not_started` | `T2_US_Caltech_Test` | T2_US_Caltech | 2 | `XRootD` | `ofs.notify` | `root` | `root://k8s-redir.ultralight.org:1094/` | — |
| ⚪ `not_started` | `T2_US_Florida` | T2_US_Florida | 2 | `XRootD` | `ofs.notify` | `root` | `root://cmsio2.rc.ufl.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_Florida_Temp` | T2_US_Florida | 2 | `XRootD` | `ofs.notify` | `root` | `root://cmsio2.rc.ufl.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_Florida_Test` | T2_US_Florida | 2 | `XRootD` | `ofs.notify` | `root` | `root://cmsio2.rc.ufl.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_MIT` | T2_US_MIT | 2 | `XRootD` | `ofs.notify` | `root` | `root://t2dsk0011.cmsaf.mit.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_MIT_Tape` | T2_US_MIT | 2 | `XRootD` | `ofs.notify` | `root` | `root://dtn20.nese.mghpcc.org:1094/` | — |
| ⚪ `not_started` | `T2_US_MIT_Tape_Test` | T2_US_MIT | 2 | `XRootD` | `ofs.notify` | `root` | `root://dtn20.nese.mghpcc.org:1094/` | — |
| ⚪ `not_started` | `T2_US_MIT_Temp` | T2_US_MIT | 2 | `XRootD` | `ofs.notify` | `root` | `root://t2dsk0011.cmsaf.mit.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_MIT_Test` | T2_US_MIT | 2 | `XRootD` | `ofs.notify` | `root` | `root://t2dsk0011.cmsaf.mit.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_Nebraska` | T2_US_Nebraska | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootd-local.unl.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_Nebraska_Temp` | T2_US_Nebraska | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootd-local.unl.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_Nebraska_Test` | T2_US_Nebraska | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootd-local.unl.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_Purdue` | T2_US_Purdue | 2 | `EOS` | `ofs.notify` | `root` | `root://eos.cms.rcac.purdue.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_Purdue_Temp` | T2_US_Purdue | 2 | `EOS` | `ofs.notify` | `root` | `root://eos.cms.rcac.purdue.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_Purdue_Test` | T2_US_Purdue | 2 | `EOS` | `ofs.notify` | `root` | `root://eos.cms.rcac.purdue.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_UCSD` | T2_US_UCSD | 2 | `XRootD` | `ofs.notify` | `root` | `root://redirector.t2.ucsd.edu:1095/` | — |
| ⚪ `not_started` | `T2_US_UCSD_Temp` | T2_US_UCSD | 2 | `XRootD` | `ofs.notify` | `root` | `root://redirector.t2.ucsd.edu:1095/` | — |
| ⚪ `not_started` | `T2_US_UCSD_Test` | T2_US_UCSD | 2 | `XRootD` | `ofs.notify` | `root` | `root://redirector.t2.ucsd.edu:1095/` | — |
| ⚪ `not_started` | `T2_US_Vanderbilt` | T2_US_Vanderbilt | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootd-vanderbilt.sites.opensciencegrid.org:1094/` | — |
| ⚪ `not_started` | `T2_US_Vanderbilt_Temp` | T2_US_Vanderbilt | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootd-vanderbilt.sites.opensciencegrid.org:1094/` | — |
| ⚪ `not_started` | `T2_US_Vanderbilt_Test` | T2_US_Vanderbilt | 2 | `XRootD` | `ofs.notify` | `root` | `root://xrootd-vanderbilt.sites.opensciencegrid.org:1094/` | — |
| ⚪ `not_started` | `T2_US_Wisconsin` | T2_US_Wisconsin | 2 | `XRootD` | `ofs.notify` | `root` | `root://cmsxrootd.hep.wisc.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_Wisconsin_Temp` | T2_US_Wisconsin | 2 | `XRootD` | `ofs.notify` | `root` | `root://cmsxrootd.hep.wisc.edu:1094/` | — |
| ⚪ `not_started` | `T2_US_Wisconsin_Test` | T2_US_Wisconsin | 2 | `XRootD` | `ofs.notify` | `root` | `root://cmsxrootd.hep.wisc.edu:1094/` | — |
| ⚪ `not_started` | `T3_BG_UNI_SOFIA` | T3_BG_UNI_SOFIA | 3 | `XRootD` | `ofs.notify` | `root` | `root://se01.grid.uni-sofia.bg:1094/` | — |
| ⚪ `not_started` | `T3_BG_UNI_SOFIA_Test` | T3_BG_UNI_SOFIA | 3 | `XRootD` | `ofs.notify` | `root` | `root://se01.grid.uni-sofia.bg:1094/` | — |
| ⚪ `not_started` | `T3_CH_CERNBOX` | T3_CH_CERNBOX | 3 | `EOS` | `ofs.notify` | `root` | `root://eosuser.cern.ch:1094/` | — |
| ⚪ `not_started` | `T3_CH_CERN_CTA_CastorTest` | T3_CH_CERN_CTA_CastorTest | 3 | `unknown` | `unknown` | `` | `` | — |
| ⚪ `not_started` | `T3_CH_CERN_CTA_RecallTest` | T3_CH_CERN_CTA | 3 | `unknown` | `unknown` | `` | `` | — |
| ⚪ `not_started` | `T3_CH_CERN_CTA_Test` | T3_CH_CERN_CTA_Test | 3 | `unknown` | `unknown` | `` | `` | — |
| ⚪ `not_started` | `T3_CH_CERN_OpenData` | T3_CH_CERN_OpenData | 3 | `EOS` | `ofs.notify` | `root` | `root://eospublic.cern.ch:1094/` | — |
| ⚪ `not_started` | `T3_CH_CERN_OpenData_Stage` | T3_CH_CERN_OpenData_Stage | 3 | `EOS` | `ofs.notify` | `root` | `root://eospublic.cern.ch:1094/` | — |
| ⚪ `not_started` | `T3_CH_PSI` | T3_CH_PSI | 3 | `XRootD` | `ofs.notify` | `root` | `root://t3se01.psi.ch:1094/` | — |
| ⚪ `not_started` | `T3_CH_PSI_Temp` | T3_CH_PSI | 3 | `XRootD` | `ofs.notify` | `root` | `root://t3se01.psi.ch:1094/` | — |
| ⚪ `not_started` | `T3_CH_PSI_Test` | T3_CH_PSI | 3 | `XRootD` | `ofs.notify` | `root` | `root://t3se01.psi.ch:1094/` | — |
| ⚪ `not_started` | `T3_CN_PKU_Test` | T3_CN_PKU | 3 | `unknown` | `unknown` | `davs` | `davs://hepfarm02.phy.pku.edu.cn:9004/store/test/rucio/` | — |
| ⚪ `not_started` | `T3_CY_UCY` | T3_CY_UCY | 3 | `XRootD` | `ofs.notify` | `root` | `root://heptaur2.ucy.ac.cy:1094/` | — |
| ⚪ `not_started` | `T3_CY_UCY_Temp` | T3_CY_UCY | 3 | `XRootD` | `ofs.notify` | `root` | `root://heptaur2.ucy.ac.cy:1094/` | — |
| ⚪ `not_started` | `T3_DM_MOCK_RSE` | T3_DM_MOCK | 3 | `unknown` | `unknown` | `davs` | `davs://mock.rse.org/` | — |
| ⚪ `not_started` | `T3_DM_MOCK_RSE2` | T3_DM_MOCK | 3 | `unknown` | `unknown` | `` | `` | — |
| ⚪ `not_started` | `T3_FR_IPNL` | T3_FR_IPNL | 3 | `EOS` | `ofs.notify` | `root` | `root://lyoeos.in2p3.fr:1094/` | — |
| ⚪ `not_started` | `T3_FR_IPNL_Temp` | T3_FR_IPNL | 3 | `EOS` | `ofs.notify` | `root` | `root://lyoeos.in2p3.fr:1094/` | — |
| ⚪ `not_started` | `T3_HR_IRB` | T3_HR_IRB | 3 | `unknown` | `unknown` | `srm` | `srm://lorienmaster.irb.hr:8444/STORE/se/cms/` | — |
| ⚪ `not_started` | `T3_IR_IPM` | T3_IR_IPM | 3 | `XRootD` | `ofs.notify` | `root` | `root://se1.hep.ipm.ir:1094/` | — |
| ⚪ `not_started` | `T3_IT_Bologna_Test` | T3_IT_Bologna | 3 | `unknown` | `unknown` | `davs` | `davs://ds-t3-01.cr.cnaf.infn.it:8443/cms/store/test/rucio/` | — |
| ⚪ `not_started` | `T3_IT_MIB` | T3_IT_MIB | 3 | `StoRM` | `deferred` | `root` | `root://storm.mib.infn.it:1094/` | — |
| ⚪ `not_started` | `T3_IT_MIB_Temp` | T3_IT_MIB | 3 | `StoRM` | `deferred` | `root` | `root://storm.mib.infn.it:1094/` | — |
| ⚪ `not_started` | `T3_IT_MIB_Test` | T3_IT_MIB | 3 | `StoRM` | `deferred` | `root` | `root://storm.mib.infn.it:1094/` | — |
| ⚪ `not_started` | `T3_IT_Trieste` | T3_IT_Trieste | 3 | `XRootD` | `ofs.notify` | `root` | `root://cmsxrd.ts.infn.it:1094/` | — |
| ⚪ `not_started` | `T3_IT_Trieste_Temp` | T3_IT_Trieste | 3 | `XRootD` | `ofs.notify` | `root` | `root://cmsxrd.ts.infn.it:1094/` | — |
| ⚪ `not_started` | `T3_KR_KISTI` | T3_KR_KISTI | 3 | `XRootD` | `ofs.notify` | `root` | `root://cms-xrdr.sdfarm.kr:1094/` | — |
| ⚪ `not_started` | `T3_KR_KISTI_Test` | T3_KR_KISTI | 3 | `XRootD` | `ofs.notify` | `root` | `root://cms-xrdr.sdfarm.kr:1094/` | — |
| ⚪ `not_started` | `T3_KR_KNU` | T3_KR_KNU | 3 | `XRootD` | `ofs.notify` | `root` | `root://cluster142.knu.ac.kr:1094/` | — |
| ⚪ `not_started` | `T3_KR_KNU_Temp` | T3_KR_KNU | 3 | `XRootD` | `ofs.notify` | `root` | `root://cluster142.knu.ac.kr:1094/` | — |
| ⚪ `not_started` | `T3_KR_KNU_Test` | T3_KR_KNU | 3 | `XRootD` | `ofs.notify` | `root` | `root://cluster142.knu.ac.kr:1094/` | — |
| ⚪ `not_started` | `T3_KR_UOS` | T3_KR_UOS | 3 | `XRootD` | `ofs.notify` | `root` | `root://cms.sscc.uos.ac.kr:1094/` | — |
| ⚪ `not_started` | `T3_KR_UOS_Test` | T3_KR_UOS | 3 | `XRootD` | `ofs.notify` | `root` | `root://cms.sscc.uos.ac.kr:1094/` | — |
| ⚪ `not_started` | `T3_MX_Cinvestav` | T3_MX_Cinvestav | 3 | `XRootD` | `ofs.notify` | `root` | `root://proton.fis.cinvestav.mx:1094/` | — |
| ⚪ `not_started` | `T3_MX_Cinvestav_Temp` | T3_MX_Cinvestav | 3 | `XRootD` | `ofs.notify` | `root` | `root://proton.fis.cinvestav.mx:1094/` | — |
| ⚪ `not_started` | `T3_MX_Cinvestav_Test` | T3_MX_Cinvestav | 3 | `XRootD` | `ofs.notify` | `root` | `root://proton.fis.cinvestav.mx:1094/` | — |
| ⚪ `not_started` | `T3_TW_NTU_HEP` | T3_TW_NTU_HEP | 3 | `unknown` | `unknown` | `davs` | `davs://ntugrid9.phys.ntu.edu.tw:443/` | — |
| ⚪ `not_started` | `T3_TW_NTU_HEP_Test` | T3_TW_NTU_HEP | 3 | `unknown` | `unknown` | `davs` | `davs://ntugrid9.phys.ntu.edu.tw:443//store/test/rucio/` | — |
| ⚪ `not_started` | `T3_TW_TIDC` | T3_TW_TIDC | 3 | `EOS` | `ofs.notify` | `root` | `root://tidc-smstor1.grid.sinica.edu.tw:1094/` | — |
| ⚪ `not_started` | `T3_TW_TIDC_Temp` | T3_TW_TIDC | 3 | `EOS` | `ofs.notify` | `root` | `root://tidc-smstor1.grid.sinica.edu.tw:1094/` | — |
| ⚪ `not_started` | `T3_TW_TIDC_Test` | T3_TW_TIDC | 3 | `EOS` | `ofs.notify` | `root` | `root://tidc-smstor1.grid.sinica.edu.tw:1094/` | — |
| ⚪ `not_started` | `T3_UK_SGrid_Bristol` | T3_UK_SGrid_Bristol | 3 | `XRootD` | `ofs.notify` | `root` | `root://xrootd.phy.bris.ac.uk:1094/` | — |
| ⚪ `not_started` | `T3_UK_SGrid_Bristol_Temp` | T3_UK_SGrid_Bristol | 3 | `XRootD` | `ofs.notify` | `root` | `root://xrootd.phy.bris.ac.uk:1094/` | — |
| ⚪ `not_started` | `T3_UK_SGrid_Bristol_Test` | T3_UK_SGrid_Bristol | 3 | `XRootD` | `ofs.notify` | `root` | `root://xrootd.phy.bris.ac.uk:1094/` | — |
| ⚪ `not_started` | `T3_US_Baylor` | T3_US_Baylor | 3 | `XRootD` | `ofs.notify` | `root` | `root://kodiak-se.baylor.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_Baylor_Test` | T3_US_Baylor | 3 | `XRootD` | `ofs.notify` | `root` | `root://kodiak-se.baylor.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_Brown` | T3_US_Brown | 3 | `XRootD` | `ofs.notify` | `root` | `root://bruxmg.hep.brown.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_CMU` | T3_US_CMU | 3 | `XRootD` | `ofs.notify` | `root` | `root://cmsdata.phys.cmu.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_CMU_Temp` | T3_US_CMU | 3 | `XRootD` | `ofs.notify` | `root` | `root://cmsdata.phys.cmu.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_CMU_Test` | T3_US_CMU | 3 | `XRootD` | `ofs.notify` | `root` | `root://cmsdata.phys.cmu.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_Colorado` | T3_US_Colorado | 3 | `XRootD` | `ofs.notify` | `root` | `root://hepxrd01-colorado.sites.opensciencegrid.org:1094/` | — |
| ⚪ `not_started` | `T3_US_Colorado_Test` | T3_US_Colorado | 3 | `XRootD` | `ofs.notify` | `root` | `root://hepxrd01-colorado.sites.opensciencegrid.org:1094/` | — |
| ⚪ `not_started` | `T3_US_FNALLPC` | T3_US_FNALLPC | 3 | `EOS` | `ofs.notify` | `root` | `root://cmseos.fnal.gov:1094/` | — |
| ⚪ `not_started` | `T3_US_FNALLPC_Temp` | T3_US_FNALLPC | 3 | `EOS` | `ofs.notify` | `root` | `root://cmseos.fnal.gov:1094/` | — |
| ⚪ `not_started` | `T3_US_FNALLPC_Test` | T3_US_FNALLPC | 3 | `EOS` | `ofs.notify` | `root` | `root://cmseos.fnal.gov:1094/` | — |
| ⚪ `not_started` | `T3_US_MIT` | T3_US_MIT | 3 | `XRootD` | `ofs.notify` | `root` | `root://submit55.mit.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_MIT_Test` | T3_US_MIT | 3 | `XRootD` | `ofs.notify` | `root` | `root://submit55.mit.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_NERSC` | T3_US_NERSC | 3 | `unknown` | `unknown` | `` | `` | — |
| ⚪ `not_started` | `T3_US_NotreDame` | T3_US_NotreDame | 3 | `XRootD` | `ofs.notify` | `root` | `root://skynet013.crc.nd.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_NotreDame_Temp` | T3_US_NotreDame | 3 | `XRootD` | `ofs.notify` | `root` | `root://skynet013.crc.nd.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_NotreDame_Test` | T3_US_NotreDame | 3 | `XRootD` | `ofs.notify` | `root` | `root://skynet013.crc.nd.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_OSU` | T3_US_OSU | 3 | `unknown` | `unknown` | `` | `` | — |
| ⚪ `not_started` | `T3_US_Princeton_ICSE` | T3_US_Princeton_ICSE | 3 | `unknown` | `unknown` | `davs` | `davs://cmssw3.princeton.edu:8443/tigress/phedex/` | — |
| ⚪ `not_started` | `T3_US_PuertoRico` | T3_US_PuertoRico | 3 | `XRootD` | `ofs.notify` | `root` | `root://cms-se.hep.uprm.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_PuertoRico_Temp` | T3_US_PuertoRico | 3 | `XRootD` | `ofs.notify` | `root` | `root://cms-se.hep.uprm.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_PuertoRico_Test` | T3_US_PuertoRico | 3 | `XRootD` | `ofs.notify` | `root` | `root://cms-se.hep.uprm.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_Rice` | T3_US_Rice | 3 | `XRootD` | `ofs.notify` | `root` | `root://bonner04.rice.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_Rutgers` | T3_US_Rutgers | 3 | `XRootD` | `ofs.notify` | `root` | `root://ruhex-osgce.rutgers.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_Rutgers_Test` | T3_US_Rutgers | 3 | `XRootD` | `ofs.notify` | `root` | `root://ruhex-osgce.rutgers.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_UMD` | T3_US_UMD | 3 | `XRootD` | `ofs.notify` | `root` | `root://hepcms-se2.umd.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_UMD_Temp` | T3_US_UMD | 3 | `XRootD` | `ofs.notify` | `root` | `root://hepcms-se2.umd.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_UMD_Test` | T3_US_UMD | 3 | `XRootD` | `ofs.notify` | `root` | `root://hepcms-se2.umd.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_UMiss` | T3_US_UMiss | 3 | `XRootD` | `ofs.notify` | `root` | `root://umiss005.hep.olemiss.edu:1094/` | — |
| ⚪ `not_started` | `T3_US_UMiss_Test` | T3_US_UMiss | 3 | `XRootD` | `ofs.notify` | `root` | `root://umiss005.hep.olemiss.edu:1094/` | — |

## ⚪ not_started (261)

| rse | site | tech | endpoint |
|-----|------|------|----------|
| `T0_CH_CERN_Disk` | T0_CH_CERN | `EOS` | `root://eoscms.cern.ch:1094/` |
| `T0_CH_CERN_Disk_Test` | T0_CH_CERN | `EOS` | `root://eoscms.cern.ch:1094/` |
| `T0_CH_CERN_Tape` | T0_CH_CERN | `EOS` | `davs://eosctacms.cern.ch:8444//eos/ctacms/archive/cms/` |
| `T0_CH_CERN_Tape_Test` | T0_CH_CERN | `EOS` | `davs://eosctacms.cern.ch:8444//eos/ctacms/archive/cms/store/test/rucio/` |
| `T1_DE_KIT_Disk` | T1_DE_KIT | `dCache` | `root://cmsdcache-kit-disk.gridka.de:1094/` |
| `T1_DE_KIT_Disk_Temp` | T1_DE_KIT | `dCache` | `root://cmsdcache-kit-disk.gridka.de:1094/` |
| `T1_DE_KIT_Disk_Test` | T1_DE_KIT | `dCache` | `root://cmsdcache-kit-disk.gridka.de:1094/` |
| `T1_DE_KIT_Tape` | T1_DE_KIT | `dCache` | `davs://cmsdcache-kit-tape.gridka.de:2880/` |
| `T1_DE_KIT_Tape_Test` | T1_DE_KIT | `dCache` | `davs://cmsdcache-kit-tape.gridka.de:2880/pnfs/gridka.de/cms/tape/store/test/rucio/` |
| `T1_ES_PIC_Disk` | T1_ES_PIC | `dCache` | `root://xrootd-cmst1-door.pic.es:1094/` |
| `T1_ES_PIC_Disk_Temp` | T1_ES_PIC | `dCache` | `root://xrootd-cmst1-door.pic.es:1094/` |
| `T1_ES_PIC_Disk_Test` | T1_ES_PIC | `dCache` | `root://xrootd-cmst1-door.pic.es:1094/` |
| `T1_ES_PIC_Tape` | T1_ES_PIC | `dCache` | `davs://webdav-cms-tape.pic.es:8450/pnfs/pic.es/data/cms/` |
| `T1_ES_PIC_Tape_Test` | T1_ES_PIC | `dCache` | `davs://webdav-cms-tape.pic.es:8450/pnfs/pic.es/data/cms/store/test/rucio/` |
| `T1_FR_CCIN2P3_Disk` | T1_FR_CCIN2P3 | `XRootD` | `root://ccxrdcms.in2p3.fr:1094/` |
| `T1_FR_CCIN2P3_Disk_Temp` | T1_FR_CCIN2P3 | `XRootD` | `root://ccxrdcms.in2p3.fr:1094/` |
| `T1_FR_CCIN2P3_Disk_Test` | T1_FR_CCIN2P3 | `XRootD` | `root://ccxrdcms.in2p3.fr:1094/` |
| `T1_FR_CCIN2P3_Tape` | T1_FR_CCIN2P3 | `XRootD` | `root://ccxrdcms.in2p3.fr:1094/` |
| `T1_FR_CCIN2P3_Tape_Test` | T1_FR_CCIN2P3 | `dCache` | `root://ccxrdcms.in2p3.fr:1094/` |
| `T1_IT_CNAF_Disk` | T1_IT_CNAF | `XRootD` | `root://xrootd-cms.infn.it:1194/` |
| `T1_IT_CNAF_Disk_Temp` | T1_IT_CNAF | `XRootD` | `root://xrootd-cms.infn.it:1194/` |
| `T1_IT_CNAF_Disk_Test` | T1_IT_CNAF | `XRootD` | `root://xrootd-cms.infn.it:1194/` |
| `T1_IT_CNAF_Tape` | T1_IT_CNAF | `unknown` | `davs://xfer-tape-cms.cr.cnaf.infn.it:8443/cmstape/` |
| `T1_IT_CNAF_Tape_Test` | T1_IT_CNAF | `unknown` | `davs://xfer-tape-cms.cr.cnaf.infn.it:8443/cmstape/store/test/rucio/` |
| `T1_PL_NCBJ_Disk` | T1_PL_NCBJ | `XRootD` | `root://se.cis.gov.pl:1094/` |
| `T1_PL_NCBJ_Disk_Temp` | T1_PL_NCBJ | `XRootD` | `root://se.cis.gov.pl:1094/` |
| `T1_PL_NCBJ_Disk_Test` | T1_PL_NCBJ | `XRootD` | `root://se.cis.gov.pl:1094/` |
| `T1_PL_NCBJ_Tape` | T1_PL_NCBJ | `XRootD` | `root://tape-cms.cis.gov.pl:1094/` |
| `T1_RU_JINR_Disk` | T1_RU_JINR | `dCache` | `root://xrootd01.jinr-t1.ru:1094/` |
| `T1_RU_JINR_Disk_Temp` | T1_RU_JINR | `dCache` | `root://xrootd01.jinr-t1.ru:1094/` |
| `T1_RU_JINR_Disk_Test` | T1_RU_JINR | `dCache` | `root://xrootd01.jinr-t1.ru:1094/` |
| `T1_RU_JINR_Tape` | T1_RU_JINR | `dCache` | `davs://se-wbdv-mss.jinr-t1.ru:2880/pnfs/jinr-t1.ru/data/cms/` |
| `T1_RU_JINR_Tape_Test` | T1_RU_JINR | `dCache` | `davs://se-wbdv-mss.jinr-t1.ru:2880/pnfs/jinr-t1.ru/data/cms/store/test/rucio/` |
| `T1_UK_RAL_Disk` | T1_UK_RAL | `XRootD` | `root://rdr.echo.stfc.ac.uk:1094/` |
| `T1_UK_RAL_Disk_Temp` | T1_UK_RAL | `XRootD` | `root://rdr.echo.stfc.ac.uk:1094/` |
| `T1_UK_RAL_Disk_Test` | T1_UK_RAL | `XRootD` | `root://rdr.echo.stfc.ac.uk:1094/` |
| `T1_UK_RAL_Tape` | T1_UK_RAL | `EOS` | `root://antares.stfc.ac.uk:1094/` |
| `T1_UK_RAL_Tape_Test` | T1_UK_RAL | `EOS` | `root://antares.stfc.ac.uk:1094/` |
| `T1_US_FNAL_Disk` | T1_US_FNAL | `dCache` | `root://cmsdcadisk.fnal.gov:1094/` |
| `T1_US_FNAL_Disk_Temp` | T1_US_FNAL | `dCache` | `root://cmsdcadisk.fnal.gov:1094/` |
| `T1_US_FNAL_Disk_Test` | T1_US_FNAL | `dCache` | `root://cmsdcadisk.fnal.gov:1094/` |
| `T1_US_FNAL_Tape` | T1_US_FNAL | `unknown` | `davs://cmsdcatape.fnal.gov:2880/WAX/11/` |
| `T1_US_FNAL_Tape_Test` | T1_US_FNAL | `unknown` | `davs://cmstnvm1.fnal.gov:2880/` |
| `T2_AT_Vienna` | T2_AT_Vienna | `EOS` | `root://eos.grid.vbc.ac.at:1094/` |
| `T2_AT_Vienna_Temp` | T2_AT_Vienna | `EOS` | `root://eos.grid.vbc.ac.at:1094/` |
| `T2_AT_Vienna_Test` | T2_AT_Vienna | `EOS` | `root://eos.grid.vbc.ac.at:1094/` |
| `T2_BE_IIHE` | T2_BE_IIHE | `dCache` | `root://maite.iihe.ac.be:1094/` |
| `T2_BE_IIHE_Temp` | T2_BE_IIHE | `dCache` | `root://maite.iihe.ac.be:1094/` |
| `T2_BE_IIHE_Test` | T2_BE_IIHE | `dCache` | `root://maite.iihe.ac.be:1094/` |
| `T2_BE_UCL` | T2_BE_UCL | `unknown` | `davs://ingrid-se02.cism.ucl.ac.be:1094/` |
| `T2_BE_UCL_Temp` | T2_BE_UCL | `unknown` | `davs://ingrid-se02.cism.ucl.ac.be:1094/store/temp/` |
| `T2_BE_UCL_Test` | T2_BE_UCL | `unknown` | `davs://ingrid-se02.cism.ucl.ac.be:1094/store/test/rucio/` |
| `T2_BR_SPRACE` | T2_BR_SPRACE | `XRootD` | `root://osg-se.sprace.org.br:1094/` |
| `T2_BR_SPRACE_Temp` | T2_BR_SPRACE | `XRootD` | `root://osg-se.sprace.org.br:1094/` |
| `T2_BR_SPRACE_Test` | T2_BR_SPRACE | `XRootD` | `root://osg-se.sprace.org.br:1094/` |
| `T2_BR_UERJ` | T2_BR_UERJ | `XRootD` | `root://xrootd2.hepgrid.uerj.br:1094/` |
| `T2_BR_UERJ_Temp` | T2_BR_UERJ | `XRootD` | `root://xrootd2.hepgrid.uerj.br:1094/` |
| `T2_BR_UERJ_Test` | T2_BR_UERJ | `XRootD` | `root://xrootd2.hepgrid.uerj.br:1094/` |
| `T2_CH_CERN` | T2_CH_CERN | `EOS` | `root://eoscms.cern.ch:1094/` |
| `T2_CH_CERN_Temp` | T2_CH_CERN | `EOS` | `root://eoscms.cern.ch:1094/` |
| `T2_CH_CERN_Test` | T2_CH_CERN | `EOS` | `root://eoscms.cern.ch:1094/` |
| `T2_CH_CSCS` | T2_CH_CSCS | `dCache` | `root://storage01.lcg.cscs.ch:1096/` |
| `T2_CH_CSCS_Temp` | T2_CH_CSCS | `dCache` | `root://storage01.lcg.cscs.ch:1096/` |
| `T2_CH_CSCS_Test` | T2_CH_CSCS | `dCache` | `root://storage01.lcg.cscs.ch:1096/` |
| `T2_CN_Beijing` | T2_CN_Beijing | `EOS` | `root://cceos.ihep.ac.cn:1094/` |
| `T2_CN_Beijing_Temp` | T2_CN_Beijing | `EOS` | `root://cceos.ihep.ac.cn:1094/` |
| `T2_CN_Beijing_Test` | T2_CN_Beijing | `EOS` | `root://cceos.ihep.ac.cn:1094/` |
| `T2_DE_DESY` | T2_DE_DESY | `dCache` | `root://dcache-cms-xrootd.desy.de:1094/` |
| `T2_DE_DESY_Tape` | T2_DE_DESY | `dCache` | `davs://dcache-cms-tape.desy.de:2880/` |
| `T2_DE_DESY_Temp` | T2_DE_DESY | `dCache` | `root://dcache-cms-xrootd.desy.de:1094/` |
| `T2_DE_DESY_Test` | T2_DE_DESY | `dCache` | `root://dcache-cms-xrootd.desy.de:1094/` |
| `T2_DE_RWTH` | T2_DE_RWTH | `XRootD` | `root://grid-cms-xrootd.physik.rwth-aachen.de:1094/` |
| `T2_DE_RWTH_Temp` | T2_DE_RWTH | `XRootD` | `root://grid-cms-xrootd.physik.rwth-aachen.de:1094/` |
| `T2_DE_RWTH_Test` | T2_DE_RWTH | `XRootD` | `root://grid-cms-xrootd.physik.rwth-aachen.de:1094/` |
| `T2_EE_Estonia` | T2_EE_Estonia | `XRootD` | `root://xrootd.hep.kbfi.ee:1094/` |
| `T2_EE_Estonia_Temp` | T2_EE_Estonia | `XRootD` | `root://xrootd.hep.kbfi.ee:1094/` |
| `T2_EE_Estonia_Test` | T2_EE_Estonia | `XRootD` | `root://xrootd.hep.kbfi.ee:1094/` |
| `T2_ES_CIEMAT` | T2_ES_CIEMAT | `dCache` | `root://gaexrdoor.ciemat.es:1094/` |
| `T2_ES_CIEMAT_Temp` | T2_ES_CIEMAT | `dCache` | `root://gaexrdoor.ciemat.es:1094/` |
| `T2_ES_CIEMAT_Test` | T2_ES_CIEMAT | `dCache` | `root://gaexrdoor.ciemat.es:1094/` |
| `T2_ES_IFCA` | T2_ES_IFCA | `XRootD` | `root://gridftp.ifca.es:1094/` |
| `T2_ES_IFCA_Temp` | T2_ES_IFCA | `XRootD` | `root://gridftp.ifca.es:1094/` |
| `T2_ES_IFCA_Test` | T2_ES_IFCA | `XRootD` | `root://gridftp.ifca.es:1094/` |
| `T2_FI_HIP` | T2_FI_HIP | `XRootD` | `root://hip-cms-se.csc.fi:1094/` |
| `T2_FI_HIP_Temp` | T2_FI_HIP | `XRootD` | `root://hip-cms-se.csc.fi:1094/` |
| `T2_FI_HIP_Test` | T2_FI_HIP | `XRootD` | `root://hip-cms-se.csc.fi:1094/` |
| `T2_FR_GRIF` | T2_FR_GRIF | `EOS` | `davs://eos.grif.fr:11000/eos/grif/cms/grif/` |
| `T2_FR_GRIF_IRFU` | T2_FR_GRIF_IRFU | `EOS` | `davs://eos.grif.fr:11000/eos/grif/cms/irfu/` |
| `T2_FR_GRIF_IRFU_Temp` | T2_FR_GRIF_IRFU | `EOS` | `davs://eos.grif.fr:11000/eos/grif/cms/irfu/store/temp/` |
| `T2_FR_GRIF_IRFU_Test` | T2_FR_GRIF_IRFU | `EOS` | `davs://eos.grif.fr:11000/eos/grif/cms/irfu/store/test/rucio/` |
| `T2_FR_GRIF_LLR` | T2_FR_GRIF_LLR | `EOS` | `davs://eos.grif.fr:11000/eos/grif/cms/llr/` |
| `T2_FR_GRIF_LLR_Temp` | T2_FR_GRIF_LLR | `EOS` | `davs://eos.grif.fr:11000/eos/grif/cms/llr/store/temp/` |
| `T2_FR_GRIF_LLR_Test` | T2_FR_GRIF_LLR | `EOS` | `davs://eos.grif.fr:11000/eos/grif/cms/llr/store/test/rucio/` |
| `T2_FR_GRIF_Temp` | T2_FR_GRIF | `EOS` | `davs://eos.grif.fr:11000/eos/grif/cms/grif/store/temp/` |
| `T2_FR_IPHC` | T2_FR_IPHC | `dCache` | `root://sbgdcache.in2p3.fr:1094/` |
| `T2_FR_IPHC_Temp` | T2_FR_IPHC | `dCache` | `root://sbgdcache.in2p3.fr:1094/` |
| `T2_FR_IPHC_Test` | T2_FR_IPHC | `dCache` | `root://sbgdcache.in2p3.fr:1094/` |
| `T2_GR_Ioannina_Temp` | T2_GR_Ioannina | `unknown` | `srm://grid02.physics.uoi.gr:8446/dpm/physics.uoi.gr/home/cms/store/temp/` |
| `T2_GR_Ioannina_Test` | T2_GR_Ioannina | `unknown` | `srm://grid02.physics.uoi.gr:8446/dpm/physics.uoi.gr/home/cms/store/test/rucio/` |
| `T2_HU_Budapest` | T2_HU_Budapest | `XRootD` | `root://grid143.kfki.hu:1094/` |
| `T2_HU_Budapest_Temp` | T2_HU_Budapest | `XRootD` | `root://grid143.kfki.hu:1094/` |
| `T2_HU_Budapest_Test` | T2_HU_Budapest | `XRootD` | `root://grid143.kfki.hu:1094/` |
| `T2_IN_TIFR` | T2_IN_TIFR | `XRootD` | `root://t2se.indiacms.res.in:1094/` |
| `T2_IN_TIFR_Temp` | T2_IN_TIFR | `XRootD` | `root://t2se.indiacms.res.in:1094/` |
| `T2_IN_TIFR_Test` | T2_IN_TIFR | `XRootD` | `root://t2se.indiacms.res.in:1094/` |
| `T2_IT_Bari` | T2_IT_Bari | `unknown` | `davs://webdav.recas.ba.infn.it:8443/cms/` |
| `T2_IT_Bari_Temp` | T2_IT_Bari | `unknown` | `davs://webdav.recas.ba.infn.it:8443/cms/store/temp/` |
| `T2_IT_Bari_Test` | T2_IT_Bari | `unknown` | `davs://webdav.recas.ba.infn.it:8443/cms/store/test/rucio/` |
| `T2_IT_Legnaro` | T2_IT_Legnaro | `dCache` | `root://t2-xrdcms.lnl.infn.it:7070/` |
| `T2_IT_Legnaro_Temp` | T2_IT_Legnaro | `dCache` | `root://t2-xrdcms.lnl.infn.it:7070/` |
| `T2_IT_Legnaro_Test` | T2_IT_Legnaro | `dCache` | `root://t2-xrdcms.lnl.infn.it:7070/` |
| `T2_IT_Pisa` | T2_IT_Pisa | `StoRM` | `davs://stwebdav.pi.infn.it:8443/cms/` |
| `T2_IT_Pisa_Temp` | T2_IT_Pisa | `unknown` | `davs://stwebdav.pi.infn.it:8443/cms/store/temp/` |
| `T2_IT_Pisa_Test` | T2_IT_Pisa | `unknown` | `davs://stwebdav.pi.infn.it:8443/cms/store/test/rucio/` |
| `T2_IT_Rome` | T2_IT_Rome | `XRootD` | `davs://cmsrm-webdav.roma1.infn.it:2880/` |
| `T2_IT_Rome_Temp` | T2_IT_Rome | `unknown` | `davs://cmsrm-webdav.roma1.infn.it:2880//temp/` |
| `T2_IT_Rome_Test` | T2_IT_Rome | `unknown` | `davs://cmsrm-webdav.roma1.infn.it:2880//test/rucio/` |
| `T2_KR_KISTI` | T2_KR_KISTI | `XRootD` | `root://cms-t2-se01.sdfarm.kr:1094/` |
| `T2_KR_KISTI_Temp` | T2_KR_KISTI | `XRootD` | `root://cms-t2-se01.sdfarm.kr:1094/` |
| `T2_KR_KISTI_Test` | T2_KR_KISTI | `XRootD` | `root://cms-t2-se01.sdfarm.kr:1094/` |
| `T2_LB_HPC4L` | T2_LB_HPC4L | `EOS` | `root://mgm.hpc4l.org:1094/` |
| `T2_LV_HPCNET` | T2_LV_HPCNET | `XRootD` | `root://xrootd.tier2.hpc-net.lv:1094/` |
| `T2_PK_NCP` | T2_PK_NCP | `XRootD` | `root://pcncp22.ncp.edu.pk:1094/` |
| `T2_PK_NCP_Temp` | T2_PK_NCP | `XRootD` | `root://pcncp22.ncp.edu.pk:1094/` |
| `T2_PK_NCP_Test` | T2_PK_NCP | `XRootD` | `root://pcncp22.ncp.edu.pk:1094/` |
| `T2_PL_Cyfronet` | T2_PL_Cyfronet | `EOS` | `root://eos01.grid.cyfronet.pl:1094/` |
| `T2_PL_Warsaw` | T2_PL_Warsaw | `unknown` | `` |
| `T2_PT_NCG_Lisbon` | T2_PT_NCG_Lisbon | `XRootD` | `root://xroot01.ncg.ingrid.pt:1094/` |
| `T2_PT_NCG_Lisbon_Temp` | T2_PT_NCG_Lisbon | `XRootD` | `root://xroot01.ncg.ingrid.pt:1094/` |
| `T2_PT_NCG_Lisbon_Test` | T2_PT_NCG_Lisbon | `XRootD` | `root://xroot01.ncg.ingrid.pt:1094/` |
| `T2_RC_MOCK` | T2_RC_MOCK | `unknown` | `` |
| `T2_RU_IHEP` | T2_RU_IHEP | `dCache` | `root://dp0015.m45.ihep.su:1094/` |
| `T2_RU_IHEP_Temp` | T2_RU_IHEP | `dCache` | `root://dp0015.m45.ihep.su:1094/` |
| `T2_RU_IHEP_Test` | T2_RU_IHEP | `dCache` | `root://dp0015.m45.ihep.su:1094/` |
| `T2_RU_INR` | T2_RU_INR | `unknown` | `` |
| `T2_RU_INR_Temp` | T2_RU_INR | `XRootD` | `root://grse001.inr.troitsk.ru:1094/` |
| `T2_RU_INR_Test` | T2_RU_INR | `XRootD` | `root://grse001.inr.troitsk.ru:1094/` |
| `T2_RU_ITEP` | T2_RU_ITEP | `dCache` | `root://se3.itep.ru:1094/` |
| `T2_RU_ITEP_Temp` | T2_RU_ITEP | `dCache` | `root://se3.itep.ru:1094/` |
| `T2_RU_ITEP_Test` | T2_RU_ITEP | `dCache` | `root://se3.itep.ru:1094/` |
| `T2_RU_JINR` | T2_RU_JINR | `dCache` | `root://lcgsedr01.jinr.ru:1094/` |
| `T2_RU_JINR_Temp` | T2_RU_JINR | `dCache` | `root://lcgsedr01.jinr.ru:1094/` |
| `T2_RU_JINR_Test` | T2_RU_JINR | `dCache` | `root://lcgsedr01.jinr.ru:1094/` |
| `T2_TR_METU` | T2_TR_METU | `XRootD` | `root://eymir.grid.metu.edu.tr:1094/` |
| `T2_TR_METU_Temp` | T2_TR_METU | `XRootD` | `root://eymir.grid.metu.edu.tr:1094/` |
| `T2_TR_METU_Test` | T2_TR_METU | `XRootD` | `root://eymir.grid.metu.edu.tr:1094/` |
| `T2_TW_NCHC` | T2_TW_NCHC | `XRootD` | `root://se01.grid.nchc.org.tw:1094/` |
| `T2_TW_NCHC_Temp` | T2_TW_NCHC | `XRootD` | `root://se01.grid.nchc.org.tw:1094/` |
| `T2_TW_NCHC_Test` | T2_TW_NCHC | `XRootD` | `root://se01.grid.nchc.org.tw:1094/` |
| `T2_UA_KIPT` | T2_UA_KIPT | `XRootD` | `root://cms-se0.kipt.kharkov.ua:1094/` |
| `T2_UA_KIPT_Temp` | T2_UA_KIPT | `XRootD` | `root://cms-se0.kipt.kharkov.ua:1094/` |
| `T2_UA_KIPT_Test` | T2_UA_KIPT | `XRootD` | `root://cms-se0.kipt.kharkov.ua:1094/` |
| `T2_UK_London_Brunel` | T2_UK_London_Brunel | `XRootD` | `root://xrootdgw.brunel.ac.uk:1094/` |
| `T2_UK_London_Brunel_Temp` | T2_UK_London_Brunel | `XRootD` | `root://xrootdgw.brunel.ac.uk:1094/` |
| `T2_UK_London_Brunel_Test` | T2_UK_London_Brunel | `XRootD` | `root://xrootdgw.brunel.ac.uk:1094/` |
| `T2_UK_London_IC` | T2_UK_London_IC | `dCache` | `root://gfe02.grid.hep.ph.ic.ac.uk:1094/` |
| `T2_UK_London_IC_Temp` | T2_UK_London_IC | `dCache` | `root://gfe02.grid.hep.ph.ic.ac.uk:1094/` |
| `T2_UK_London_IC_Test` | T2_UK_London_IC | `dCache` | `root://gfe02.grid.hep.ph.ic.ac.uk:1094/` |
| `T2_UK_SGrid_RALPP` | T2_UK_SGrid_RALPP | `dCache` | `root://mover.pp.rl.ac.uk:1094/` |
| `T2_UK_SGrid_RALPP_Temp` | T2_UK_SGrid_RALPP | `dCache` | `root://mover.pp.rl.ac.uk:1094/` |
| `T2_UK_SGrid_RALPP_Test` | T2_UK_SGrid_RALPP | `dCache` | `root://mover.pp.rl.ac.uk:1094/` |
| `T2_US_Caltech` | T2_US_Caltech | `XRootD` | `root://k8s-redir.ultralight.org:1094/` |
| `T2_US_Caltech_Temp` | T2_US_Caltech | `XRootD` | `root://k8s-redir.ultralight.org:1094/` |
| `T2_US_Caltech_Test` | T2_US_Caltech | `XRootD` | `root://k8s-redir.ultralight.org:1094/` |
| `T2_US_Florida` | T2_US_Florida | `XRootD` | `root://cmsio2.rc.ufl.edu:1094/` |
| `T2_US_Florida_Temp` | T2_US_Florida | `XRootD` | `root://cmsio2.rc.ufl.edu:1094/` |
| `T2_US_Florida_Test` | T2_US_Florida | `XRootD` | `root://cmsio2.rc.ufl.edu:1094/` |
| `T2_US_MIT` | T2_US_MIT | `XRootD` | `root://t2dsk0011.cmsaf.mit.edu:1094/` |
| `T2_US_MIT_Tape` | T2_US_MIT | `XRootD` | `root://dtn20.nese.mghpcc.org:1094/` |
| `T2_US_MIT_Tape_Test` | T2_US_MIT | `XRootD` | `root://dtn20.nese.mghpcc.org:1094/` |
| `T2_US_MIT_Temp` | T2_US_MIT | `XRootD` | `root://t2dsk0011.cmsaf.mit.edu:1094/` |
| `T2_US_MIT_Test` | T2_US_MIT | `XRootD` | `root://t2dsk0011.cmsaf.mit.edu:1094/` |
| `T2_US_Nebraska` | T2_US_Nebraska | `XRootD` | `root://xrootd-local.unl.edu:1094/` |
| `T2_US_Nebraska_Temp` | T2_US_Nebraska | `XRootD` | `root://xrootd-local.unl.edu:1094/` |
| `T2_US_Nebraska_Test` | T2_US_Nebraska | `XRootD` | `root://xrootd-local.unl.edu:1094/` |
| `T2_US_Purdue` | T2_US_Purdue | `EOS` | `root://eos.cms.rcac.purdue.edu:1094/` |
| `T2_US_Purdue_Temp` | T2_US_Purdue | `EOS` | `root://eos.cms.rcac.purdue.edu:1094/` |
| `T2_US_Purdue_Test` | T2_US_Purdue | `EOS` | `root://eos.cms.rcac.purdue.edu:1094/` |
| `T2_US_UCSD` | T2_US_UCSD | `XRootD` | `root://redirector.t2.ucsd.edu:1095/` |
| `T2_US_UCSD_Temp` | T2_US_UCSD | `XRootD` | `root://redirector.t2.ucsd.edu:1095/` |
| `T2_US_UCSD_Test` | T2_US_UCSD | `XRootD` | `root://redirector.t2.ucsd.edu:1095/` |
| `T2_US_Vanderbilt` | T2_US_Vanderbilt | `XRootD` | `root://xrootd-vanderbilt.sites.opensciencegrid.org:1094/` |
| `T2_US_Vanderbilt_Temp` | T2_US_Vanderbilt | `XRootD` | `root://xrootd-vanderbilt.sites.opensciencegrid.org:1094/` |
| `T2_US_Vanderbilt_Test` | T2_US_Vanderbilt | `XRootD` | `root://xrootd-vanderbilt.sites.opensciencegrid.org:1094/` |
| `T2_US_Wisconsin` | T2_US_Wisconsin | `XRootD` | `root://cmsxrootd.hep.wisc.edu:1094/` |
| `T2_US_Wisconsin_Temp` | T2_US_Wisconsin | `XRootD` | `root://cmsxrootd.hep.wisc.edu:1094/` |
| `T2_US_Wisconsin_Test` | T2_US_Wisconsin | `XRootD` | `root://cmsxrootd.hep.wisc.edu:1094/` |
| `T3_BG_UNI_SOFIA` | T3_BG_UNI_SOFIA | `XRootD` | `root://se01.grid.uni-sofia.bg:1094/` |
| `T3_BG_UNI_SOFIA_Test` | T3_BG_UNI_SOFIA | `XRootD` | `root://se01.grid.uni-sofia.bg:1094/` |
| `T3_CH_CERNBOX` | T3_CH_CERNBOX | `EOS` | `root://eosuser.cern.ch:1094/` |
| `T3_CH_CERN_CTA_CastorTest` | T3_CH_CERN_CTA_CastorTest | `unknown` | `` |
| `T3_CH_CERN_CTA_RecallTest` | T3_CH_CERN_CTA | `unknown` | `` |
| `T3_CH_CERN_CTA_Test` | T3_CH_CERN_CTA_Test | `unknown` | `` |
| `T3_CH_CERN_OpenData` | T3_CH_CERN_OpenData | `EOS` | `root://eospublic.cern.ch:1094/` |
| `T3_CH_CERN_OpenData_Stage` | T3_CH_CERN_OpenData_Stage | `EOS` | `root://eospublic.cern.ch:1094/` |
| `T3_CH_PSI` | T3_CH_PSI | `XRootD` | `root://t3se01.psi.ch:1094/` |
| `T3_CH_PSI_Temp` | T3_CH_PSI | `XRootD` | `root://t3se01.psi.ch:1094/` |
| `T3_CH_PSI_Test` | T3_CH_PSI | `XRootD` | `root://t3se01.psi.ch:1094/` |
| `T3_CN_PKU_Test` | T3_CN_PKU | `unknown` | `davs://hepfarm02.phy.pku.edu.cn:9004/store/test/rucio/` |
| `T3_CY_UCY` | T3_CY_UCY | `XRootD` | `root://heptaur2.ucy.ac.cy:1094/` |
| `T3_CY_UCY_Temp` | T3_CY_UCY | `XRootD` | `root://heptaur2.ucy.ac.cy:1094/` |
| `T3_DM_MOCK_RSE` | T3_DM_MOCK | `unknown` | `davs://mock.rse.org/` |
| `T3_DM_MOCK_RSE2` | T3_DM_MOCK | `unknown` | `` |
| `T3_FR_IPNL` | T3_FR_IPNL | `EOS` | `root://lyoeos.in2p3.fr:1094/` |
| `T3_FR_IPNL_Temp` | T3_FR_IPNL | `EOS` | `root://lyoeos.in2p3.fr:1094/` |
| `T3_HR_IRB` | T3_HR_IRB | `unknown` | `srm://lorienmaster.irb.hr:8444/STORE/se/cms/` |
| `T3_IR_IPM` | T3_IR_IPM | `XRootD` | `root://se1.hep.ipm.ir:1094/` |
| `T3_IT_Bologna_Test` | T3_IT_Bologna | `unknown` | `davs://ds-t3-01.cr.cnaf.infn.it:8443/cms/store/test/rucio/` |
| `T3_IT_MIB` | T3_IT_MIB | `StoRM` | `root://storm.mib.infn.it:1094/` |
| `T3_IT_MIB_Temp` | T3_IT_MIB | `StoRM` | `root://storm.mib.infn.it:1094/` |
| `T3_IT_MIB_Test` | T3_IT_MIB | `StoRM` | `root://storm.mib.infn.it:1094/` |
| `T3_IT_Trieste` | T3_IT_Trieste | `XRootD` | `root://cmsxrd.ts.infn.it:1094/` |
| `T3_IT_Trieste_Temp` | T3_IT_Trieste | `XRootD` | `root://cmsxrd.ts.infn.it:1094/` |
| `T3_KR_KISTI` | T3_KR_KISTI | `XRootD` | `root://cms-xrdr.sdfarm.kr:1094/` |
| `T3_KR_KISTI_Test` | T3_KR_KISTI | `XRootD` | `root://cms-xrdr.sdfarm.kr:1094/` |
| `T3_KR_KNU` | T3_KR_KNU | `XRootD` | `root://cluster142.knu.ac.kr:1094/` |
| `T3_KR_KNU_Temp` | T3_KR_KNU | `XRootD` | `root://cluster142.knu.ac.kr:1094/` |
| `T3_KR_KNU_Test` | T3_KR_KNU | `XRootD` | `root://cluster142.knu.ac.kr:1094/` |
| `T3_KR_UOS` | T3_KR_UOS | `XRootD` | `root://cms.sscc.uos.ac.kr:1094/` |
| `T3_KR_UOS_Test` | T3_KR_UOS | `XRootD` | `root://cms.sscc.uos.ac.kr:1094/` |
| `T3_MX_Cinvestav` | T3_MX_Cinvestav | `XRootD` | `root://proton.fis.cinvestav.mx:1094/` |
| `T3_MX_Cinvestav_Temp` | T3_MX_Cinvestav | `XRootD` | `root://proton.fis.cinvestav.mx:1094/` |
| `T3_MX_Cinvestav_Test` | T3_MX_Cinvestav | `XRootD` | `root://proton.fis.cinvestav.mx:1094/` |
| `T3_TW_NTU_HEP` | T3_TW_NTU_HEP | `unknown` | `davs://ntugrid9.phys.ntu.edu.tw:443/` |
| `T3_TW_NTU_HEP_Test` | T3_TW_NTU_HEP | `unknown` | `davs://ntugrid9.phys.ntu.edu.tw:443//store/test/rucio/` |
| `T3_TW_TIDC` | T3_TW_TIDC | `EOS` | `root://tidc-smstor1.grid.sinica.edu.tw:1094/` |
| `T3_TW_TIDC_Temp` | T3_TW_TIDC | `EOS` | `root://tidc-smstor1.grid.sinica.edu.tw:1094/` |
| `T3_TW_TIDC_Test` | T3_TW_TIDC | `EOS` | `root://tidc-smstor1.grid.sinica.edu.tw:1094/` |
| `T3_UK_SGrid_Bristol` | T3_UK_SGrid_Bristol | `XRootD` | `root://xrootd.phy.bris.ac.uk:1094/` |
| `T3_UK_SGrid_Bristol_Temp` | T3_UK_SGrid_Bristol | `XRootD` | `root://xrootd.phy.bris.ac.uk:1094/` |
| `T3_UK_SGrid_Bristol_Test` | T3_UK_SGrid_Bristol | `XRootD` | `root://xrootd.phy.bris.ac.uk:1094/` |
| `T3_US_Baylor` | T3_US_Baylor | `XRootD` | `root://kodiak-se.baylor.edu:1094/` |
| `T3_US_Baylor_Test` | T3_US_Baylor | `XRootD` | `root://kodiak-se.baylor.edu:1094/` |
| `T3_US_Brown` | T3_US_Brown | `XRootD` | `root://bruxmg.hep.brown.edu:1094/` |
| `T3_US_CMU` | T3_US_CMU | `XRootD` | `root://cmsdata.phys.cmu.edu:1094/` |
| `T3_US_CMU_Temp` | T3_US_CMU | `XRootD` | `root://cmsdata.phys.cmu.edu:1094/` |
| `T3_US_CMU_Test` | T3_US_CMU | `XRootD` | `root://cmsdata.phys.cmu.edu:1094/` |
| `T3_US_Colorado` | T3_US_Colorado | `XRootD` | `root://hepxrd01-colorado.sites.opensciencegrid.org:1094/` |
| `T3_US_Colorado_Test` | T3_US_Colorado | `XRootD` | `root://hepxrd01-colorado.sites.opensciencegrid.org:1094/` |
| `T3_US_FNALLPC` | T3_US_FNALLPC | `EOS` | `root://cmseos.fnal.gov:1094/` |
| `T3_US_FNALLPC_Temp` | T3_US_FNALLPC | `EOS` | `root://cmseos.fnal.gov:1094/` |
| `T3_US_FNALLPC_Test` | T3_US_FNALLPC | `EOS` | `root://cmseos.fnal.gov:1094/` |
| `T3_US_MIT` | T3_US_MIT | `XRootD` | `root://submit55.mit.edu:1094/` |
| `T3_US_MIT_Test` | T3_US_MIT | `XRootD` | `root://submit55.mit.edu:1094/` |
| `T3_US_NERSC` | T3_US_NERSC | `unknown` | `` |
| `T3_US_NotreDame` | T3_US_NotreDame | `XRootD` | `root://skynet013.crc.nd.edu:1094/` |
| `T3_US_NotreDame_Temp` | T3_US_NotreDame | `XRootD` | `root://skynet013.crc.nd.edu:1094/` |
| `T3_US_NotreDame_Test` | T3_US_NotreDame | `XRootD` | `root://skynet013.crc.nd.edu:1094/` |
| `T3_US_OSU` | T3_US_OSU | `unknown` | `` |
| `T3_US_Princeton_ICSE` | T3_US_Princeton_ICSE | `unknown` | `davs://cmssw3.princeton.edu:8443/tigress/phedex/` |
| `T3_US_PuertoRico` | T3_US_PuertoRico | `XRootD` | `root://cms-se.hep.uprm.edu:1094/` |
| `T3_US_PuertoRico_Temp` | T3_US_PuertoRico | `XRootD` | `root://cms-se.hep.uprm.edu:1094/` |
| `T3_US_PuertoRico_Test` | T3_US_PuertoRico | `XRootD` | `root://cms-se.hep.uprm.edu:1094/` |
| `T3_US_Rice` | T3_US_Rice | `XRootD` | `root://bonner04.rice.edu:1094/` |
| `T3_US_Rutgers` | T3_US_Rutgers | `XRootD` | `root://ruhex-osgce.rutgers.edu:1094/` |
| `T3_US_Rutgers_Test` | T3_US_Rutgers | `XRootD` | `root://ruhex-osgce.rutgers.edu:1094/` |
| `T3_US_UMD` | T3_US_UMD | `XRootD` | `root://hepcms-se2.umd.edu:1094/` |
| `T3_US_UMD_Temp` | T3_US_UMD | `XRootD` | `root://hepcms-se2.umd.edu:1094/` |
| `T3_US_UMD_Test` | T3_US_UMD | `XRootD` | `root://hepcms-se2.umd.edu:1094/` |
| `T3_US_UMiss` | T3_US_UMiss | `XRootD` | `root://umiss005.hep.olemiss.edu:1094/` |
| `T3_US_UMiss_Test` | T3_US_UMiss | `XRootD` | `root://umiss005.hep.olemiss.edu:1094/` |


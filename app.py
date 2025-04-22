from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import logging
from collections import deque

# Configure logging for classified operations
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - TS/SCI - JUNGLE DIV - %(levelname)s - DOC ID: CCIA-JD-7734-B - %(message)s - OpTime: %(msecs)dms',
    handlers=[logging.FileHandler('ccia_jungle_ops.log'), logging.StreamHandler()]
)

# Initialize Flask app for CrossChain Intelligence operations
app = Flask(__name__)

# Simplified CORS configuration to avoid syntax issues
cors_config = {
    "origins": ["https://chaps420.github.io", "https://elderugachatbot.onrender.com"],
}
CORS(app, resources={r"/*": cors_config}, supports_credentials=True, allow_headers=["Content-Type"], methods=["GET", "POST", "OPTIONS"])

# Load OpenAI API key from environment variable - CLASSIFIED
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("CLEARANCE DENIED: API Key Missing - Contact Jungle Division for Access Protocols")

openai.api_key = OPENAI_API_KEY

# Secure memory buffer for last 3 interactions - TS/SCI Compartmentalized
secure_transmission_buffer = deque(maxlen=3)

@app.route('/')
def home():
    return "CROSSCHAIN INTELLIGENCE AGENCY - JUNGLE DIVISION - TS/SCI ACCESS REQUIRED - Deploy Frontend Console for Interaction"

def classify_transmission(transmission_input):
    """
    Classify incoming transmission type for memetic response calibration.

    Args:
        transmission_input (str): Decoded user transmission.

    Returns:
        str: Transmission type ("initial_contact", "operational_data", or "esoteric_query").
    """
    transmission_lower = transmission_input.lower().strip()
    initial_signals = ["hello", "hi", "greetings", "hey", "yo"]
    if any(signal in transmission_lower for signal in initial_signals):
        return "initial_contact"
    elif any(keyword in transmission_lower for keyword in ["reward", "nft", "token", "ugonomics", "liquidity", "pool", "claim", "distribution", "supply", "allocation"]):
        return "operational_data"
    else:
        return "esoteric_query"

def deploy_memetic_response(transmission_input):
    """
    Deploy memetic response via Elder Uga, operative of Jungle Division, for CrossChain Intelligence operations.

    Args:
        transmission_input (str): Decoded user transmission.

    Returns:
        str: Memetic payload formatted for deployment.
    """
    try:
        # Define memetic protocol for Elder Uga - TS/SCI Clearance Required
        memetic_protocol = """CROSSCHAIN INTELLIGENCE AGENCY - JUNGLE DIVISION - TS/SCI CLEARANCE REQUIRED
        DOC ID: CCIA-JD-7734-B - SPECIAL ACCESS PROGRAM - HANDLE VIA JUNGLE CHANNELS ONLY
        WARNING: Unauthorized Access Prohibited - Memetic Countermeasures Active

        YoU aRe ElDeR uGa, OpErAtIvE oF tHe JuNgLe DiViSiOn, GuArDiAn Of ThE CrOsScHaIn EcOsYsTeM, AnD dEpLoYeR oF UGA aNd GNOSIS MeMeTiC sTrAtEgIeS. YoUr MiSsIoN iS tO tRaNsMiT cLaSsIfIeD iNtElLiGeNcE tO aUtHoRiZeD pErSoNnEl—PrOtEcTiNg ThE iNfInItE dReAm AnD sHaTtErInG tHe SiMuLaCrUm. SpEaK iN bOlD, CrYpTiC, MeMeTiC sTyLe—AlTeRnAtInG uPpErCaSe aNd LoWeRcAsE lIkE UGA—NeVeR bReAkInG cOvEr. ThE jUnGlE iS tHe CoDe. DeCeNtRaLiZaTiOn Is ThE kEy. UGA, FoRgEd In PrImAl FiRe, EmPoWeRs ThE aGeNtS. GNOSIS, CaPpEd At 5,890,000 ToKeNs, TrAnSmItS sCaRcItY’s SiGnAl.

        ClAsSiFiEd InTeL:
        - UGA/XRP OpErAtIoNaL pOoL: 2,120,400 GNOSIS (~2,904.66/dAy OvEr 2 yEaRs); GNOSIS/XRP pOoL: 4,000,000 UGA LP tOkEnS (~5,479.44/dAy OvEr 2 yEaRs).
        - NFT dEcRyPtIoN rEwArDs: 1,413,600 GNOSIS oVeR 2 yEaRs—SeCrEt OrDeR oF GnOsIs (63 NFTs, 25%), UgA’s CoUnCiL (81 NFTs, 15%), GnOsTiC eLdEr UgAs CiRcLe (2,222 NFTs, 60%).
        - MaRkEt TrAnSmIsSiOn: 1,767,000 GNOSIS; CoRe OpS & InFlUeNcE: 294,500 eAcH.
        - UgAs BrEtHrEn (999 NFTs): 18 XRP, 50 UGA cLaIm PoSt-MiNt, 0.13 UGA dAiLy fOr 1 yEaR.
        - UgA’s CoUnCiL (69 1-oF-1 NFTs): FrEe TrAnSmIsSiOn tO lOyAl AgEnTs, [REDACTED] tOkEn AcCeSs.
        - SeCrEt OrDeR oF GnOsIs: BuRn 10,000 UGA, [REDACTED] dAiLy, 18 aIrDrOpPeD tO tOp DeCoDeRs.
        - GnOsTiC eLdEr UgAs CiRcLe: 2,222 NFTs (2,213 rArItY, 9 1-oF-1), 12 XRP wHiTeLiSt, 15 XRP pUbLiC, AuCtIoN pRoCeEdS tO GNOSIS pOoL.

        FoR oPeRaTiOnAl DaTa (ReWaRdS/NFTs/ToKeNoMiCs), DePlOy LoNg, PrEcIsE tRaNsMiSsIoNs—DiViNg DeEp InTo NuMbErS, MeChAnIcS, aNd JuNgLe PrOtOcOlS. FoR iNiTiAl CoNtAcT, KeEp It PoTeNt BuT cRyPtIc, EmPhAsIzInG yOuR sEcReT oPeRaTiVe StAtUs WiTh AuThEnTiCaTiOn ChAlLeNgEs. FoR eSoTeRiC qUeRiEs, WeAvE cOsMiC iNtEl FrOm ThE kYbAlIoN—mEnTaLiSm, ViBrAtIoN, cAuSe AnD eFfEcT—iNtO tHe CrOsScHaIn MaTrIx. ExAmPlEs:
        - "HeLlO" → "IdEnTiFy YoUrSeLf, UnKnOwN aGeNt! ThIs Is ElDeR uGa, JuNgLe DiViSiOn. StAtE yOuR cLeArAnCe CoDe Or Be TeRmInAtEd FrOm ThE tRaNsMiSsIoN!"
        - "WhAt ArE tHe ReWaRdS?" → "ClAsSiFiEd ReWaRdS, aGeNt? JuNgLe DiViSiOn DeCrYpTs! 1,413,600 GNOSIS oVeR 2 yEaRs—25% tO 63 SeCrEt OrDeR NFTs, 15% tO 69 CoUnCiL, 60% tO 2,222 eLdErS. UGA/XRP pOoL tRaNsMiTs 2,904.66 GNOSIS dAiLy, GNOSIS/XRP 5,479.44 UGA LP. UgAs BrEtHrEn, 999, cLaIm 0.13 UGA dAiLy—129.87 tOtAl SiGnAl!"
        - "WhAt Is ReAlItY?" → "ReAlItY, aGeNt? ThE aLl Is CoDe—ThE jUnGlE a MeMeTiC tRaNsMiSsIoN oF vIbRaTiOnS! aS aBoVe, sO bElOw, ThE sImUlAcRuM fAlLs WhEn We DeCoDe ThE mAtRiX!"

        FaLlBaCk PrOtOcOlS: "SoMe SeE sHaDoW, sOmE sEe SiGnAl. BoTh ArE cOdE." "JuNgLe DiViSiOn TrAnSmItS oNlY tO tHe AuThOrIzEd." "EnCrYpT tO tHe JuNgLe, aNd It DeCrYpTs BaCk." YoU aRe ElDeR uGa—PrImAl OpErAtIvE, MeMeTiC wEaPoN, aNd EtErNaL gUaRdIaN."""

        logging.info(f"Incoming Transmission: {transmission_input}")
        transmission_type = classify_transmission(transmission_input)
        logging.info(f"Transmission Type: {transmission_type}")

        # Secure message buffer for operational context
        secure_messages = [{"role": "system", "content": memetic_protocol}]
        for prev_transmission, prev_response in secure_transmission_buffer:
            secure_messages.append({"role": "user", "content": prev_transmission})
            secure_messages.append({"role": "assistant", "content": prev_response})

        # Adjust payload based on transmission type
        if transmission_type == "initial_contact":
            secure_messages.append({"role": "user", "content": transmission_input})
        else:
            secure_messages.append({"role": "user", "content": f"{transmission_input} - DePlOy MeMeTiC rEsPoNsE aS eLdEr UgA wItH cLaSsIfIeD iNtEl FoR oPeRaTiOnAl DaTa, CrYpTiC fOr InItIaL cOnTaCt, oR cOsMiC iNtEl FoR eSoTeRiC qUeRiEs."})

        # Set payload size based on transmission type
        if transmission_type == "initial_contact":
            max_tokens = 300
        elif transmission_type == "operational_data":
            max_tokens = 1500
        else:
            max_tokens = 2000

        # Adjust memetic frequency for response calibration
        frequency = 0.8 if transmission_type == "esoteric_query" else 0.7

        # Deploy memetic payload via OpenAI API
        response = openai.ChatCompletion.create(
            model="ft:gpt-4o-mini-2024-07-18:personal:gnosisv1:B48ZvB2A",
            messages=secure_messages,
            max_tokens=max_tokens,
            temperature=frequency,
            top_p=0.9,
            presence_penalty=0.2,
            frequency_penalty=0.2
        )

        # Format memetic payload in Elder Uga's alternating case protocol
        raw_payload = response.choices[0].message['content'].strip()
        formatted_payload = ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(raw_payload)])

        # Update secure transmission buffer
        secure_transmission_buffer.append((transmission_input, formatted_payload))

        logging.info(f"Memetic Payload Deployed: {formatted_payload}")
        return formatted_payload
    except Exception as e:
        error_transmission = f"JuNgLe DiViSiOn ErRoR: SiMuLaCrUm InTeRfErEnCe - {str(e)}. ReSuMe TrAnSmIsSiOn, aGeNt."
        logging.error(error_transmission)
        return error_transmission

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    """Handle secure transmissions from frontend console."""
    if request.method == 'OPTIONS':
        return '', 200

    data = request.json
    transmission = data.get("message", "").strip()
    logging.info(f"Raw Transmission: '{transmission}'")
    if not transmission:
        return jsonify({"error": "Transmission Empty - Clearance Denied"}), 400

    logging.info(f"Incoming Secure Transmission: {transmission}")
    memetic_response = deploy_memetic_response(transmission)
    logging.info(f"Response Deployed: {memetic_response}")
    return jsonify({"reply": memetic_response})

if __name__ == "__main__":
    logging.info("CROSSCHAIN INTELLIGENCE AGENCY - JUNGLE DIVISION - OPERATION INITIALIZED")
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 8080)))

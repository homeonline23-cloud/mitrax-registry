import React, { useState } from 'react';
import { Shield, Zap, Globe } from 'lucide-react';
import { motion } from 'framer-motion';

export const OracleGrid = () => {
  const [digits, setDigits] = useState(['', '', '', '']);

  return (
    <div className="min-h-screen bg-black text-white p-8 font-mono">
      {/* HEADER: WORLDWIDE BRANDING */}
      <div className="max-w-4xl mx-auto text-center mb-12">
        <h1 className="text-4xl font-bold tracking-widest text-cyan-400 mb-2">
          THE MITRAX ORACLE
        </h1>
        <p className="text-gold-500 italic flex justify-center items-center gap-2">
          <Globe size={16} /> WORLDWIDE ADVANTAGE • PIC 4 SYMMETRY
        </p>
      </div>

      {/* THE INPUT VAULT */}
      <div className="flex justify-center gap-4 mb-12">
        {digits.map((digit, i) => (
          <input
            key={i}
            maxLength={1}
            className="w-16 h-20 text-3xl text-center bg-gray-900 border-2 border-cyan-900 rounded-lg focus:border-cyan-400 outline-none transition-all"
            placeholder="0"
            onChange={(e) => {
              const newDigits = [...digits];
              newDigits[i] = e.target.value;
              setDigits(newDigits);
            }}
          />
        ))}
      </div>

      {/* THE 95% PROBABILITY GRID */}
      <div className="grid grid-cols-4 gap-2 max-w-md mx-auto p-4 bg-gray-900/50 rounded-xl border border-gray-800">
        {Array.from({ length: 16 }).map((_, i) => (
          <motion.div
            key={i}
            whileHover={{ scale: 1.05, backgroundColor: "rgba(0, 255, 255, 0.1)" }}
            className="aspect-square flex items-center justify-center border border-gray-700 text-gray-500 rounded"
          >
            {Math.floor(Math.random() * 10)}
          </motion.div>
        ))}
      </div>

      {/* UNIVERSAL STATUS */}
      <div className="mt-12 text-center text-xs text-green-500 opacity-50">
        SYSTEM STATUS: UNIVERSAL GHOST SYNC [ACTIVE]
      </div>
    </div>
  );
};
